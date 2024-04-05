import sys

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import col, desc



if __name__ == "__main__":
    if len(sys.argv) != 2:
       print("Usage: assignment_03 <file>", file=sys.stderr)
       sys.exit(-1)

# creating spark session
    spark = (SparkSession
    .builder
    .appName("departuredelays")
    .getOrCreate())

# defining the file path for the departuredelay csv
    departure_delay_file = sys.argv[1]

# Define schema for the flight data
    departure_delay_schema = StructType([
        StructField('date', StringType(), True),
        StructField('delay', IntegerType(), True),
        StructField('distance', IntegerType(), True),
        StructField('origin', StringType(), True),
        StructField('destination', StringType(), True)
    ])

# reading the departuredelay.csv file into the dataframe

    df = (spark.read.format("csv")
      .option("header", "true")
      .schema(departure_delay_schema)
      .load(departure_delay_file)
    )

# Part 1 Registering DataFrame as a temporary view
    df.createOrReplaceTempView("us_delay_flights_tbl")

# Part 1 - Query 1
    p1q1_result_sql = spark.sql("""SELECT date, delay, origin, destination
       FROM us_delay_flights_tbl
       WHERE delay > 120 AND ORIGIN = 'SFO' AND DESTINATION = 'ORD'
       ORDER by delay DESC""")
    print("Python(Spark SQL)- The delays which are greater than 120 from SFO and ORD:")
    p1q1_result_sql.show(10, truncate=False)

# Part 1 - Query 2
    p1q2_result_pyspark = df.select("date", "delay", "origin", "destination") \
        .filter((col("delay") > 120) & (col("origin") == "SFO") & (col("destination") == "ORD")) \
        .orderBy(desc("delay"))
    print("Python(Dataframe API)- The delays which are greater than 120 from SFO and ORD:")
    p1q2_result_pyspark.show(10, truncate=False)

# Part 2 Creating Table named us_delay_flights_tbl

    df.write.mode("overwrite").saveAsTable("us_delay_flights_tbl")

# Part 2 - Query

    p2q_result_sql = spark.sql("""CREATE OR REPLACE TEMPORARY VIEW flights_chicago_march AS
        SELECT * FROM us_delay_flights_tbl
        WHERE origin = 'ORD' AND 
        (MONTH(TO_DATE(date, 'MMddHHmm')) = 3) AND
        (DAYOFMONTH(TO_DATE(date, 'MMddHHmm')) BETWEEN 1 AND 15)
        ORDER by delay DESC""")
    print("Python- The departure delays from ORD in the month of March are:", spark.catalog.listColumns("us_delay_flights_tbl"))
    spark.sql("SELECT * FROM flights_chicago_march").show(5, truncate=False)

# Part 3 

# writing dataframe to json
    (df.write.format("json").mode("overwrite").option("compression", "none").save("departuredelays.json"))

# writing dataframe to lz4
    (df.write.format("json").mode("overwrite").option("compression", "lz4").save("departuredelays.lz4"))

# writing dataframe to parquet
    (df.write.format("parquet").mode("overwrite").option("compression", "none").save("departuredelays.parquet"))

# Part 4
# Reading departuredelays Parquet file
    parquet_df = spark.read.parquet("departuredelays.parquet")

# Filtering records with ORD as Origin and writing to orddeparturedelays
    ord_departure_delays_df = parquet_df.filter(col("origin") == "ORD")
    print("Python- The departure delays from the ORD are:")
    ord_departure_delays_df.show(10, truncate=False)

# Write the results to DataFrameWriter named orddeparturedelays
    ord_departure_delays_df.write.mode("overwrite").parquet("orddeparturedelays.parquet")



# stop spark session
spark.stop()