# 🍬 M&M Color Count Analysis using Apache Spark

## 🎯 Overview
This project analyzes M&M candy color distribution across different U.S. states using Apache Spark. It provides insights into the most popular M&M colors and their distribution patterns.

## 🛠️ Tech Stack
Apache Spark (PySpark) – Distributed data processing
DataFrame API – Data aggregation and filtering
CSV Data Handling – Reading and transforming structured data

## 📂 Dataset
The dataset consists of:
✅ State – U.S. state where M&Ms were counted
✅ Color – M&M color (e.g., Red, Blue, Yellow)
✅ Count – Number of M&Ms for each color in a state

📌 Project Breakdown
## 📊 Step 1: Data Loading
📌 Process:
1️⃣ Read CSV file into a Spark DataFrame
2️⃣ Infer schema to determine column types

## 📊 Step 2: Total M&M Count by State & Color
📌 Process:
1️⃣ Group data by State and Color
2️⃣ Sum up the count for each group
3️⃣ Sort results in descending order to find the most popular color

## 📊 Step 3: M&M Color Count in California (CA)
📌 Process:
1️⃣ Filter data to include only California (CA)
2️⃣ Group by Color and sum the counts
3️⃣ Sort results to identify the most popular color in CA

## 📊 Key Insights & Takeaways
✅ Identifies the most popular M&M color in the U.S.
✅ Analyzes state-wise color preferences
✅ Finds the top M&M color in California