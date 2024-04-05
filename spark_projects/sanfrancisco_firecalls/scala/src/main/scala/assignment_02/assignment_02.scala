package main.scala.assignment_02

import org.apache.spark.sql.{SparkSession, Encoders}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._

// Defining the case class to represent the schema of the json data
case class DeviceIoTData_schema(
  battery_level: Long, c02_level: Long, cca2: String, cca3: String,
  cn: String, device_id: Long, device_name: String, humidity: Long,
  ip: String, latitude: Double, lcd: String, longitude: Double,
  scale: String, temp: Long, timestamp: Long
)

object assignment_02 {
  def main(args: Array[String]) {
    val spark = SparkSession
      .builder
      .appName("IoTDevices")
      .getOrCreate()
    if (args.length < 1) {
      print("Usage: assignment_02 <file>")
      sys.exit(1)
    }

import spark.implicits._

 // Defining file path
    val IoTDevicesFile = args(0)
    val IoTDf = spark.read.json(IoTDevicesFile).as[DeviceIoTData_schema]

// Question 1: Detect failing devices with battery levels below a threshold.

/* 
Answer 1: The result indicates a total count of 19,851 failing devices with battery levels falling below the specified threshold of 1. 
Alongside this count, a detailed table of 20 rows is presented, providing comprehensive information about these devices. 
The table includes data on battery level, CO2 level, country, device ID, device name, humidity, IP address, location coordinates, LCD status, temperature, timestamp, and the scale of measurement.
*/

val failingDevices = IoTDf.filter(col("battery_level") < 1)
println(s"Ans1: Failing devices with battery levels below the threshold 1: ${failingDevices.count()}")
failingDevices.show(false)

// Question 2: Identify offending countries with high levels of CO2 emissions.

/*
Answer 2:The output generates a table which exhibits offending countries with CO2 levels exceeding 1,400, 
showcasing the country code (cn) and the corresponding average CO2 levels. 
The output include three countries Gabon, Falkland Islands, and Monaco, where Gabon has the highest 
average co2 levels at 1523 followed by Falkland Islan at 1424 and the Monaco at 1421.5.
*/    
    
val threshold = 1400
val highCO2Countries = IoTDf
  .groupBy("cn")
  .agg(avg("c02_level").alias("avg_co2_levels"))
  .filter(col("avg_co2_levels") > threshold)
  .select("cn", "avg_co2_levels")
  .orderBy(desc("avg_co2_levels"))
println("Ans2: The offending countries with Co2 exeeding more than 1400: ")
highCO2Countries.show(false)

// Question 3: Compute the min and max values for temperature, battery level, CO2, and humidity.
    
/* 
Answer 3: The table provides the minimum and maximum values for temperature, battery level, CO2 level, 
and humidity across all devices in the dataset.
The highlighted results indicate the minimum temperature is 10, maximum temperature is 34, minimum battery level is 0, 
maximum battery level is 9, minimum CO2 level is 800, maximum CO2 level is 1,599, minimum humidity is 25, and maximum humidity is 99.
*/

val minMaxValues = IoTDf.agg(
  min("temp").alias("min_temperature"),
  max("temp").alias("max_temperature"),
  min("battery_level").alias("min_battery_level"),
  max("battery_level").alias("max_battery_level"),
  min("c02_level").alias("min_c02_level"),
  max("c02_level").alias("max_c02_level"),
  min("humidity").alias("min_humidity"),
  max("humidity").alias("max_humidity"))
println("Ans3: The max and min temp, battery lvl, co2 and humidity are:")
minMaxValues.show(false)

// Question 4: Sort and group by average temperature, CO2, humidity, and country.
    
/*
Answer 4: The table presents the average temperature, CO2 level, and humidity for each country.
The results are sorted in ascending order based on the country code (cn). Highlighting results include 
Anguilla with the highest average temperature of 31.14 and Andorra with the highest average CO2 level 
and average humidity of 1279 and 75 respectively.
*/    
    
val avgValuesByCountry = IoTDf.where(col("cn")=!="").groupBy("cn")
  .agg(
  avg("temp").alias("avg_temperature"),
  avg("c02_level").alias("avg_c02_level"),
  avg("humidity").alias("avg_humidity"))
  .orderBy(asc("cn"))
println("Ans4: The average temp, co2 and humidity per country: ")
avgValuesByCountry.show(false)

    spark.stop()
  }
}
