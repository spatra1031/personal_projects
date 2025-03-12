# 🚒 San Francisco Fire Calls Analysis using Apache Spark

## 🎯 Overview
This project analyzes San Francisco fire department emergency call data using Apache Spark. It provides insights into the frequency, distribution, and response times of fire calls.

## 🛠️ Tech Stack
Apache Spark (PySpark & Scala) – Distributed data processing
DataFrame API & SQL Queries – Data aggregation and analysis
Parquet Storage – Efficient data retrieval and storage

## 📂 Dataset
The dataset consists of:
✅ CallNumber – Unique identifier for each call
✅ UnitID – The fire department unit responding
✅ IncidentNumber – The incident report number
✅ CallType – Type of emergency (Fire, Medical, etc.)
✅ CallDate – Date of the call
✅ Neighborhood – SF neighborhood where the call occurred
✅ Delay – Response time in minutes

## 📌 Project Breakdown

## 🔥 Step 1: Data Loading & Cleaning
📌 Process:
1️⃣ Read CSV data into a Spark DataFrame
2️⃣ Define and apply schema for structured analysis

## 📊 Step 2: Key Analysis & Insights
📌 1. What were the different types of fire calls in 2018?
✅ Extract unique fire call types reported in 2018.

📌 2. Which months had the highest fire calls in 2018?
✅ Group fire calls by month and count occurrences.
✅ Identify the busiest month for fire incidents.

📌 3. Which neighborhood generated the most fire calls in 2018?
✅ Group by neighborhood and count incidents.
✅ Find the top neighborhood with the highest calls.

📌 4. Which neighborhoods had the worst response times?
✅ Calculate average response time per neighborhood.
✅ Identify areas needing faster emergency response.

📌 5. Which week had the most fire calls in 2018?
✅ Find the busiest week for emergency calls.

📌 6. Correlation Between Neighborhood, Zip Code & Fire Calls
✅ Analyze relationships between neighborhoods, zip codes, and fire calls.

## 📊 Step 3: Storing and Querying Data
📌 Using Parquet for Faster Data Retrieval
✅ Write processed fire call data to a Parquet file
✅ Read from Parquet to enable fast queries

## 🚀 Future Enhancements
🔹 Interactive dashboards using Power BI/Tableau
🔹 Machine Learning for fire incident prediction
🔹 Real-time data streaming for live monitoring