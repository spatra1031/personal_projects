import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, current_date, when

if __name__ == "__main__":
    if len(sys.argv) > 2:
       print("Usage: assignment_04 <file>", file=sys.stderr)
       sys.exit(-1)

# creating spark session
    spark = (SparkSession
    .builder
    .appName("assignment_04")
    .getOrCreate())

# Part 1

# reading from the dataframe
    employees_df = spark.read.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/employees") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", "employees") \
        .option("user", "worker") \
        .option("password", "cluster") \
        .load()

    print("Number of records:", employees_df.count())

    employees_df.printSchema()

# Creating a DataFrame of the top 10,000 employee salaries (sort DESC) from the salaries table
    salaries_df = spark.read.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/employees") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", "(SELECT * FROM salaries ORDER BY salary DESC LIMIT 10000) AS top_salaries") \
        .option("user", "worker") \
        .option("password", "cluster") \
        .load()

# Writing the DataFrame back to database to a new table called 'aces'
    salaries_df.write.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/employees") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", "aces") \
        .option("user", "worker") \
        .option("password", "cluster") \
        .mode("overwrite")\
        .save()

# Writing the DataFrame out to the local system as a CSV and saving it to the local system using snappy compression
    salaries_df.write.mode("overwrite").csv("salaries.csv", compression="snappy")

# Part 2
# Creating a JDBC and selecting from the titles table where employees title equals Senior Engineer
    senior_engineers_df = spark.read.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/employees") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("query", "SELECT * FROM titles WHERE title = 'Senior Engineer'") \
        .option("user", "worker") \
        .option("password", "cluster") \
        .load()
    
# Temp column stating if the senior engineer employee is still with the company    
    senior_engineers_df = senior_engineers_df.withColumn("status", 
        when(col("to_date") == "9999-01-01", "current").when(col("to_date") < current_date(), "left").otherwise("NA"))

# Count how many senior engineers have left and how many are current
    left_count = senior_engineers_df.filter(col("status") == "left").count()
    current_count = senior_engineers_df.filter(col("status") == "current").count()
    print("Senior Engineers who have Left:", left_count)
    print("Senior Engineers are Currently working:", current_count)

# Senior Engineers information that have left the company
    left_senior_engineers_df = senior_engineers_df.filter(col("status") == "left")

# Creating a PySpark SQL tempView of just the Senior Engineers that have left the company
    left_senior_engineers_df.createOrReplaceTempView("left_tempview")


# Writing left_table back to the database
    (left_senior_engineers_df.write.format("jdbc") 
        .option("url", "jdbc:mysql://localhost:3306/employees") 
        .option("driver", "com.mysql.cj.jdbc.Driver") 
        .option("dbtable", "left_table") 
        .option("user", "worker") 
        .option("password", "cluster") 
        .mode("overwrite") 
        .save())

# Writing left_tempview back to the database
    (spark.sql("select * from left_tempview")
        .write.format("jdbc") 
        .option("url", "jdbc:mysql://localhost:3306/employees") 
        .option("driver", "com.mysql.cj.jdbc.Driver") 
        .option("dbtable", "left_tempview") 
        .option("user", "worker") 
        .option("password", "cluster") 
        .mode("overwrite") 
        .save())

# Writing left_df back to the database
    (left_senior_engineers_df.write.format("jdbc") 
        .option("url", "jdbc:mysql://localhost:3306/employees") 
        .option("driver", "com.mysql.cj.jdbc.Driver") 
        .option("dbtable", "left_df") 
        .option("user", "worker") 
        .option("password", "cluster") 
        .mode("overwrite") 
        .save())

# Writing the DataFrame to the database, using errorifexists
    (left_senior_engineers_df.write.format("jdbc") 
        .option("url", "jdbc:mysql://localhost:3306/employees") 
        .option("driver", "com.mysql.cj.jdbc.Driver") 
        .option("dbtable", "left_df") 
        .option("user", "worker") 
        .option("password", "cluster") 
        .mode("errorifexists") 
        .save())

# stop spark session
spark.stop()

