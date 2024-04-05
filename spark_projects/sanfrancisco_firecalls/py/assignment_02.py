import sys

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, FloatType
from pyspark.sql.functions import count, corr, avg, month, weekofyear, from_unixtime, unix_timestamp, col, first

if __name__ == "__main__":
    if len(sys.argv) != 2:
       print("Usage: assignment_02 <file>", file=sys.stderr)
       sys.exit(-1)

# creating spark session
    spark = (SparkSession
    .builder
    .appName("SFFireCalls")
    .getOrCreate())

# defining the file path for the sf-fire-calls csv
    sf_fire_call_file = sys.argv[1]

# Creating dataframe schema
    SFfire_schema = StructType([
    StructField('CallNumber', IntegerType(), True),
    StructField('UnitID', StringType(), True),
    StructField('IncidentNumber', IntegerType(), True),
    StructField('CallType', StringType(), True),
    StructField('CallDate', StringType(), True),
    StructField('WatchDate', StringType(), True),
    StructField('CallFinalDisposition', StringType(), True),
    StructField('AvailableDtTm', StringType(), True),
    StructField('Address', StringType(), True),
    StructField('City', StringType(), True),
    StructField('Zipcode', IntegerType(), True),
    StructField('Battalion', StringType(), True),
    StructField('StationArea', StringType(), True),
    StructField('Box', StringType(), True),
    StructField('OriginalPriority', StringType(), True),
    StructField('Priority', StringType(), True),
    StructField('FinalPriority', IntegerType(), True),
    StructField('ALSUnit', BooleanType(), True),
    StructField('CallTypeGroup', StringType(), True),
    StructField('NumAlarms', IntegerType(), True),
    StructField('UnitType', StringType(), True),
    StructField('UnitSequenceInCallDispatch', IntegerType(), True),
    StructField('FirePreventionDistrict', StringType(), True),
    StructField('SupervisorDistrict', StringType(), True),
    StructField('Neighborhood', StringType(), True),
    StructField('Location', StringType(), True),
    StructField('RowID', StringType(), True),
    StructField('Delay', FloatType(), True)
    ])    

# reading the sf-fire-call.csv file into the dataframe

    sf_fire_call_df = (spark.read.format("csv")
      .option("header", "true")
      .schema(SFfire_schema)
      .load(sf_fire_call_file)
    )

# What were all the different types of fire calls in 2018?
"""
Answer 1: The various types of fire calls in 2018 are listed in the table.
It includes categories like "Elevator / Escalator Rescue," "Alarms," "Odor (Strange / Unknown),"
"Citizen Assist / Service Call," "HazMat," "Vehicle Fire," "Other," "Outside Fire," "Traffic Collision," 
"Assist Police," "Gas Leak (Natural and LP Gases)," "Water Rescue," "Electrical Hazard," "Structure Fire," "Medical Incident,"
"Fuel Spill," "Smoke Investigation (Outside)," "Train / Rail Incident," "Explosion," and "Suspicious Package."
"""
types_of_fire_calls_2018 = (sf_fire_call_df
    .filter(col("CallDate")
    .endswith("2018"))
    .select("CallType")
    .distinct()
    )
print("Ans1: The different types of fire calls in 2018 are:")
types_of_fire_calls_2018.show(truncate=False)

# What months within the year 2018 saw the highest number of fire calls?
"""
Answer 2: The month with the highest number of fire calls in 2018 is October, with a total of 1,068 calls.
"""
months_highest_fire_calls_2018 = (sf_fire_call_df
    .filter(col("CallDate").endswith("2018"))
    .groupBy(month(from_unixtime(unix_timestamp("CallDate", "MM/dd/yyyy"))).alias("Month"))
    .agg(count("*").alias("TotalCalls"))
    .orderBy(col("TotalCalls").desc())
    .limit(1))
print("Ans2: The following month saw the highest number of fire calls in 2018:")
months_highest_fire_calls_2018.show(truncate=False)

# Which neighborhood in San Francisco generated the most fire calls in 2018?

"""
Answer 3: The neighborhood generating the most fire calls in San Francisco in 2018 is "Tenderloin," with a total of 1,393 calls.
"""
neighborhood_highest_fire_calls_2018 = (sf_fire_call_df
    .filter(col("CallDate").endswith('2018'))
    .groupBy("Neighborhood")
    .agg(count("*").alias("TotalCalls"))
    .orderBy(col("TotalCalls").desc())
    .limit(1))
print("Ans3: The following neighborhood in San Francisco generated the most fire calls in 2018:")
neighborhood_highest_fire_calls_2018.show(truncate=False)

# Which neighborhoods had the worst response times to fire calls in 2018?

"""
Answer 4: The neighborhoods with the worst response times to fire calls in 2018 are presented in the table. 
Notable neighborhoods include "Chinatown," "Presidio," "Treasure Island," "McLaren Park," and others, with corresponding worst response times.
"""
neighborhood_worst_response_time_2018 = (sf_fire_call_df
    .filter(col("CallDate").endswith('2018'))
    .groupBy("Neighborhood")
    .agg(avg("Delay").alias("WorstResponseTime"))
    .orderBy(col("WorstResponseTime").desc())
    .limit(10))
print("Ans4: The following neighborhoods had the worst response times to fire calls in 2018:")
neighborhood_worst_response_time_2018.show(truncate=False)   

# Which week in the year in 2018 had the most fire calls?

"""
Answer 5: The week with the most fire calls in 2018 is week 22, with a total of 259 calls.
"""
most_fire_calls_week_2018 = (sf_fire_call_df
    .filter(col("CallDate").endswith("2018"))
    .groupBy(weekofyear(from_unixtime(unix_timestamp("CallDate", "MM/dd/yyyy"))).alias("Week"))
    .agg(count("*").alias("TotalCalls"))
    .orderBy(col("TotalCalls").desc())
    .limit(1))
print("Ans5: The following neighborhoods had the most fire calls in the following week of 2018:")
most_fire_calls_week_2018.show(truncate=False)

# Is there a correlation between neighborhood, zip code, and number of fire calls?

"""
Answer 6: The correlation between neighborhood, zip code, and the number of fire calls is outlined in the table. The table shows the neighborhoodsorted in ascending order,
and includes details such as the neighborhood, zip code, and the total number of calls for each combination.
"""
correlation_neighborhood_zipcode_calls = (sf_fire_call_df
    .groupBy("Neighborhood", "Zipcode")
    .agg(count("*").alias("TotalCalls"))
    .select("Neighborhood", "Zipcode", "TotalCalls")
    .orderBy(col("Neighborhood").asc()))
print("Ans6: The correlation between neighborhood, zip code, and number of fire calls:")
correlation_neighborhood_zipcode_calls.show(truncate=False)

# How can we use Parquet files or SQL tables to store this data and read it back?

"""
Answer 7: The process of using Parquet files to store the csv data and reading it back is explained through the table.
It stores the data and then reads it back showing the exact data from the csv file such as CallNumber, UnitID, IncidentNumber,
CallType, CallDate, and various other attributes of each incident.
"""
parquet_file_path = "sf_fire_calls.parquet"
sf_fire_call_df.write.parquet(parquet_file_path)
parquet_df = spark.read.parquet(parquet_file_path)
print("Ans7: Using Parquet files to store this data and reading it back: ")
parquet_df.show(truncate=False)
    
# stop spark session
spark.stop()