import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import substring, to_date
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import year, month, avg, stddev

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: part3 <file>", file=sys.stderr)
        sys.exit(-1)

    # Creating Spark session
    spark = (SparkSession
             .builder
             .appName("part3")
             .getOrCreate())

    # Defining file path
    parquet_file = sys.argv[1]

    df = (spark.read.format("parquet").load(parquet_file))

# Extracting year and month from ObservationDate
    df = df.withColumn("Year", year("ObservationDate"))
    df = df.withColumn("Month", month("ObservationDate"))

    # Calculate average temperature per month per year
    avg_temp = df.groupBy("Year", "Month").agg(avg("AirTemperature").alias("AverageTemperature"))
    avg_temp.show(truncate=False)

    # Calculate standard deviation using average temperature
    stddev_temp = (avg_temp
                   .groupBy("Month")
                   .agg(stddev("AverageTemperature").alias("StdDevTemperature"))
                   .orderBy("Month"))
    stddev_temp.show(truncate=False)

    # Writing stddev_temp to Parquet
    stddev_temp.write.format("parquet").mode("overwrite").save("part-three.parquet")

    # Writing 12 stddev_temp results to CSV
    stddev_temp.write.format("csv").mode("overwrite").option("header", "true").save("part-three.csv")

    # Stop SparkSession
    spark.stop()
