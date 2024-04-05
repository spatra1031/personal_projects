package main.scala.assignment_03

import org.apache.spark.sql.{SparkSession, Encoders}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._

object assignment_03 {
  def main(args: Array[String]) {
    val spark = SparkSession
      .builder
      .appName("departuredelays")
      .getOrCreate()
    if (args.length < 1) {
      print("Usage: assignment_03 <file>")
      sys.exit(1)
    }

    import spark.implicits._

// Defining file path
    val departureDelaysFile = args(0)

// Defining the schema of the csv data
    val departureDelaySchema = StructType(
      Array(
        StructField("date", StringType, true),
        StructField("delay", IntegerType, true),
        StructField("distance", IntegerType, true),
        StructField("origin", StringType, true),
        StructField("destination", StringType, true)
      )
    )

// Defining the DataFrame
    val df = spark.read
      .format("csv")
      .option("header", "true")
      .schema(departureDelaySchema)
      .load(departureDelaysFile)


// Part 1 Registering DataFrame as a temporary view
    df.createOrReplaceTempView("us_delay_flights_tbl")

// Part 1 - Query 1
    val p1q1ResultSql = spark.sql("""SELECT date, delay, origin, destination
       FROM us_delay_flights_tbl
       WHERE delay > 120 AND ORIGIN = 'SFO' AND DESTINATION = 'ORD'
       ORDER by delay DESC""")
    println(s"Scala(Spark SQL)- The delays which are greater than 120 from SFO and ORD:")
    p1q1ResultSql.show(10, truncate = false)

// Part 1 - Query 2
    val p1q2ResultPySpark = df.select("date", "delay", "origin", "destination")
      .filter((col("delay") > 120) && (col("origin") === "SFO") && (col("destination") === "ORD"))
      .orderBy(desc("delay"))
    println(s"Scala(Dataframe API)- The delays which are greater than 120 from SFO and ORD:")
    p1q2ResultPySpark.show(10, truncate = false)

// Part 2 - Creating Table named us_delay_flights_tbl
    df.write.mode("overwrite").saveAsTable("us_delay_flights_tbl")

// Part 2 - Query
    val p2qResultSql = spark.sql(
      """CREATE OR REPLACE TEMPORARY VIEW flights_chicago_march AS
        |SELECT * FROM us_delay_flights_tbl
        |WHERE origin = 'ORD' AND
        |(MONTH(TO_DATE(date, 'MMddHHmm')) = 3) AND
        |(DAYOFMONTH(TO_DATE(date, 'MMddHHmm')) BETWEEN 1 AND 15)
        |ORDER by delay DESC""".stripMargin)
    println(s"Scala- The departure delays from ORD in the month of March are:", spark.catalog.listColumns("us_delay_flights_tbl"))
    spark.sql("SELECT * FROM flights_chicago_march").show(5, truncate = false)

 // Part 3 - Writing DataFrame to JSON, LZ4, Parquet
    df.write.format("json").mode("overwrite").option("compression", "none").save("departuredelays.json")
    df.write.format("json").mode("overwrite").option("compression", "lz4").save("departuredelays.lz4")
    df.write.format("parquet").mode("overwrite").option("compression", "none").save("departuredelays.parquet")

// Part 4 - Reading departuredelays Parquet file
    val parquetDf = spark.read.parquet("departuredelays.parquet")

// Filtering records with ORD as Origin and writing to orddeparturedelays
    val ord_departure_delays_df = parquetDf.filter(col("origin") === "ORD")
    println(s"Scala-The departure delays from the ORD are:")
    ord_departure_delays_df.show(10, truncate = false)

// Write the results to DataFrameWriter named orddeparturedelays
    ord_departure_delays_df.write.mode("overwrite").parquet("orddeparturedelays.parquet")


// stop spark session
    spark.stop()
  }
}