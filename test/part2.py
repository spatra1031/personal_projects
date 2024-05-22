import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import substring, to_date
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: part2 <file>", file=sys.stderr)
        sys.exit(-1)

    # Creating Spark session
    spark = (SparkSession
             .builder
             .appName("part2")
             .getOrCreate())

    # Defining file path
    test_file = sys.argv[1]

    df = (spark.read.format("text").load(test_file))

    # Applying transformations to create the splitDF DataFrame
    splitDF = df.withColumn('WeatherStation', substring(df['value'], 5, 6)) \
                .withColumn('WBAN', substring(df['value'], 11, 5)) \
                .withColumn('ObservationDate', to_date(substring(df['value'], 16, 8), 'yyyyMMdd')) \
                .withColumn('ObservationHour', substring(df['value'], 24, 4).cast(IntegerType())) \
                .withColumn('Latitude', substring(df['value'], 29, 6).cast('float') / 1000) \
                .withColumn('Longitude', substring(df['value'], 35, 7).cast('float') / 1000) \
                .withColumn('Elevation', substring(df['value'], 47, 5).cast(IntegerType())) \
                .withColumn('WindDirection', substring(df['value'], 61, 3).cast(IntegerType())) \
                .withColumn('WDQualityCode', substring(df['value'], 64, 1).cast(IntegerType())) \
                .withColumn('SkyCeilingHeight', substring(df['value'], 71, 5).cast(IntegerType())) \
                .withColumn('SCQualityCode', substring(df['value'], 76, 1).cast(IntegerType())) \
                .withColumn('VisibilityDistance', substring(df['value'], 79, 6).cast(IntegerType())) \
                .withColumn('VDQualityCode', substring(df['value'], 86, 1).cast(IntegerType())) \
                .withColumn('AirTemperature', substring(df['value'], 88, 5).cast('float') / 10) \
                .withColumn('ATQualityCode', substring(df['value'], 93, 1).cast(IntegerType())) \
                .withColumn('DewPoint', substring(df['value'], 94, 5).cast('float')) \
                .withColumn('DPQualityCode', substring(df['value'], 99, 1).cast(IntegerType())) \
                .withColumn('AtmosphericPressure', substring(df['value'], 100, 5).cast('float') / 10) \
                .withColumn('APQualityCode', substring(df['value'], 105, 1).cast(IntegerType())) \
                .drop('value')

    # Writing the splitDF DataFrame to a Parquet file
    splitDF.write.format("parquet").mode("overwrite").save("80.parquet")
    splitDF.show(truncate=False)

    spark.stop()..