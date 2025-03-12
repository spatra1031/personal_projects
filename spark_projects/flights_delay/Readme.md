# ✈️ Flight Delay Analysis using Apache Spark

## 🎯 Overview
This project analyzes flight departure delays using Apache Spark, focusing on identifying delay patterns, storing, and querying large datasets efficiently. The analysis includes processing flight delay data, querying trends, and optimizing storage with different formats.

## 🛠️ Tech Stack
Apache Spark – Distributed data processing
PySpark & Scala – Data transformation and analysis
SQL Queries – Data extraction and insights
Parquet & JSON Formats – Optimized data storage
Compression Techniques – LZ4 and Snappy for efficient storage

## 📂 Dataset
The dataset consists of flight departure delay records, including:
✅ Date & Time of departure
✅ Delay Duration (in minutes)
✅ Origin & Destination Airports
✅ Flight Distance

## 📌 Project Breakdown
## 🚀 Part 1: Delay Analysis
📌 Steps:
1️⃣ Load CSV data into a Spark DataFrame
2️⃣ Register DataFrame as a temporary SQL table (us_delay_flights_tbl)
3️⃣ Query & filter flights with delays > 120 mins from SFO to ORD
4️⃣ Compare results using Spark SQL vs DataFrame API

## 🔥 Part 2: Flight Trends for Chicago (ORD)
📌 Steps:
1️⃣ Create a Spark Table (us_delay_flights_tbl) for querying
2️⃣ Extract flights departing from ORD in March (1st-15th)
3️⃣ Create a temporary SQL view (flights_chicago_march)

## 📂 Part 3: Data Storage Optimization
📌 Steps:
1️⃣ Write delay data in multiple formats for storage efficiency:

JSON (uncompressed & LZ4 compressed)
Parquet (optimized for columnar storage)
🛫 Part 4: ORD Flight Delay Extraction
📌 Steps:
1️⃣ Read stored Parquet data
2️⃣ Filter flights with ORD as the origin
3️⃣ Save the filtered results as orddeparturedelays.parquet

## 📊 Key Insights & Takeaways
✅ Identifies significant flight delays from SFO to ORD
✅ Tracks seasonal delays for Chicago (ORD) in March
✅ Optimizes data storage with Parquet & compression techniques
✅ Compares SQL-based and DataFrame-based approaches for querying

## 🚀 Future Enhancements
🔹 Integrate with real-time flight APIs for live delay analysis
🔹 Develop dashboards (Tableau, Power BI) for visualization
🔹 Enhance predictive modeling for delay forecasting

