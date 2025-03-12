# 🚴 Divvy Trips Data Analysis using Apache Spark

## 🎯 Overview
This project analyzes Divvy bike-sharing trip data using Apache Spark. Implemented in both Python (PySpark) and Scala (Spark Core API), the project demonstrates how to process large datasets efficiently using Spark's DataFrame API, schema inference, and transformations.

## 🛠️ Tech Stack
Apache Spark – Distributed data processing
PySpark – Python interface for Spark
Scala – Functional programming for Spark
CSV Data Processing – Reading and analyzing structured trip data
DataFrame API – Schema definition, filtering, grouping

## 📌 Project Breakdown

## 📂 Dataset
The dataset consists of Divvy bike-sharing trips with details such as:
✅ Trip ID, Start & Stop time
✅ Bike ID, Trip Duration
✅ From & To Station details
✅ User Type, Gender, Birth Year

## 🐍 Python (PySpark) Implementation
📌 Steps:
1️⃣ Creates a Spark session
2️⃣ Reads trip data from a CSV file using three different schema approaches:

Infer Schema (Auto-detects data types)
StructField Schema (Explicit schema definition)
DDL Schema (Uses SQL-style schema)
3️⃣ Groups and counts trips based on destination station and gender
4️⃣ Displays the top 10 results
5️⃣ Stops the Spark session
🔗 Command to Run (Python)

spark-submit divvy_trips.py <path_to_csv>

## 🔥 Scala Implementation
📌 Steps:
1️⃣ Creates a Spark session
2️⃣ Reads trip data using Infer Schema, StructField Schema, and DDL Schema
3️⃣ Performs grouping and filtering for male riders per station
4️⃣ Displays the top 10 results
5️⃣ Stops the Spark session

🔗 Command to Run (Scala)

spark-submit --class main.scala.assignment_01.assignment_01 divvy_trips.scala <path_to_csv>

## 📊 Key Insights & Takeaways
✅ Schema Comparison: Different approaches to structuring data in Spark
✅ Data Processing with Spark: Efficient handling of large-scale data
✅ Aggregation & Filtering: Extracting insights on bike usage patterns

## 🚀 Future Enhancements
🔹 Integrate with a database (PostgreSQL, BigQuery, etc.)
🔹 Visualize trip data using a dashboard (Tableau, Power BI)
🔹 Optimize performance with partitioning & caching