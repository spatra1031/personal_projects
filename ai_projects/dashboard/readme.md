# AI-Powered Data Analysis Dashboard
A Streamlit-based interactive dashboard that allows users to upload datasets, request analysis in natural language, and receive automated SQL queries and visualizations using OpenAI's GPT model.

## Key Features
✔ Natural Language to SQL Query Generation
✔ Automated Data Visualization (Bar Chart, Line Chart, Pie Chart, Scatter Plot)
✔ CSV File Upload Support
✔ Interactive and User-Friendly UI with Streamlit
✔ In-Memory SQLite Database for Query Execution

## 1. Project Overview
This project enables data analysts and non-technical users to gain insights from datasets without writing SQL queries manually. By leveraging OpenAI’s GPT model, the system converts plain English queries into SQL statements, executes them on an in-memory SQLite database, and visualizes the results dynamically.

## 2. How It Works
### Step 1: Upload a CSV File
Users can upload a CSV file containing the dataset.
The file is automatically loaded into a Pandas DataFrame for further processing.
Example Screenshot:

### Step 2: Enter a Data Query in Natural Language
Users provide analysis requests in plain English (e.g., “Show me the total sales by month”).
The request is sent to OpenAI's GPT model, which generates a SQL query for SQLite syntax.
Example Screenshot:

### Step 3: AI-Generated SQL Query
The system automatically extracts the SQL query from the OpenAI response.
The generated SQL query is displayed for transparency.

Example Screenshot:

### Step 4: Execute the SQL Query
The dataset is stored in an in-memory SQLite database.
The SQL query is executed, and the resulting dataset is displayed.
Example Screenshot:

### Step 5: AI-Suggested Data Visualizations
OpenAI suggests chart types based on the query (Bar Chart, Line Chart, Pie Chart, Scatter Plot).
The system automatically plots the data using Matplotlib.

Example Screenshot:

## 3. Technology Stack
Programming & Frameworks
Python (Pandas, Matplotlib, SQLite)
Streamlit (for the interactive UI)
OpenAI GPT API (for SQL query generation)
APIs & Libraries
openai - Generates SQL queries
sqlite3 - Executes SQL queries in memory
matplotlib - Plots data based on AI-suggested charts
pandas - Data manipulation
## 4. Real-World Impact
This project bridges the gap between data analysis and AI, making it easy for users to gain insights from their data without SQL expertise.

🔹 Business Intelligence
Quickly analyze business performance without manual SQL queries
Automate report generation for sales, revenue, and customer trends
🔹 Data-Driven Decision Making
Instantly visualize data patterns for better insights
Helps non-technical users perform complex analysis easily
🔹 Enhancing Productivity
Reduces time spent on writing queries
Automates data visualization based on analysis requests
## 5. Future Enhancements
🔹 Multi-Table SQL Query Support for more complex datasets
🔹 Advanced AI Suggestions for better query understanding
🔹 Cloud Database Support (PostgreSQL, BigQuery)
🔹 Integration with Dashboards (Power BI, Tableau)