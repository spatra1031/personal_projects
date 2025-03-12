# 📊 Employee Data Analysis using Apache Spark
## 🎯 Overview
This project performs employee salary analysis and senior engineer workforce trends using Apache Spark and MySQL. The analysis includes extracting, transforming, and storing data efficiently in a distributed computing environment.

## 🛠️ Tech Stack
Apache Spark – Distributed data processing
PySpark – Python interface for Spark
MySQL (JDBC Connection) – Relational database for employee records
SQL Queries – Data extraction and transformation
DataFrame API – Schema definition, filtering, grouping
## 📂 Dataset
The dataset consists of employee information, including:
✅ Employee ID, Name, Department
✅ Salaries, Titles, Status (Active/Left)
✅ Start and End Dates

## 📌 Project Breakdown
## 🚀 Part 1: Salary Analysis
📌 Steps:
1️⃣ Read employee data from MySQL using JDBC
2️⃣ Extract top 10,000 highest salaries and create a new DataFrame
3️⃣ Store extracted salaries back into MySQL in a new table (aces)
4️⃣ Save salary data as a compressed CSV file (snappy compression)

## 🔥 Part 2: Senior Engineer Workforce Trends
📌 Steps:
1️⃣ Extract employee titles where title = "Senior Engineer"
2️⃣ Determine employee status (Current/Left) based on to_date column
3️⃣ Count and display the number of active vs. former senior engineers
4️⃣ Store records of former senior engineers into a temporary SQL view
5️⃣ Write data back to MySQL in multiple tables (left_table, left_tempview, left_df)

## 📊 Key Insights & Takeaways
✅ Salary Distribution: Identifies top earners in the company
✅ Employee Retention: Tracks attrition among senior engineers
✅ Data Integration: Demonstrates efficient data processing with Spark & MySQL

## 🚀 Future Enhancements
🔹 Integrate with BI tools (Tableau, Power BI) for data visualization
🔹 Analyze trends in employee promotions & salary growth
🔹 Optimize database queries for faster processing

