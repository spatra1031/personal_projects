import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openai
import sqlite3
import time
import re
from io import StringIO


# Set the page configuration
st.set_page_config(page_title="Data Analysis with OpenAI", layout="wide")

# OpenAI API Key from Streamlit Secrets
openai.api_key = st.secrets["openai"]["api_key"]

def generate_sql_query_and_chart(data, user_input):
    prompt = f"""
    Here is the data schema:
    {data.dtypes.to_string()}
    User input: {user_input}
    Generate a SQL query to analyze the data based on the user input. Use the table name 'data' and include only the SQL query without any additional explanation. Additionally, suggest multiple chart types (bar chart, line chart, pie chart, scatter plot) to visualize the result. Note: Adjust SQL for SQLite syntax, e.g., use strftime for date functions.
    """
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a data analyst."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500
            )
            response_text = response.choices[0].message["content"].strip()
            
            # Debugging output
            st.write("OpenAI Response:", response_text)

            # Use regex to extract the SQL query
            sql_query_match = re.search(r"(SELECT .*?;)", response_text, re.DOTALL)
            if sql_query_match:
                sql_query = sql_query_match.group(1).strip()
            else:
                st.error("No SQL query found in the response.")
                return None, None

            # Extract chart types
            chart_types = re.findall(r"(bar chart|line chart|pie chart|scatter plot)", response_text, re.IGNORECASE)
            if not chart_types:
                st.error("No chart type suggestions found in the response.")
                return None, None

            return sql_query, chart_types
        except Exception as e:  # Catch all exceptions
            st.error(f"An error occurred: {e}")
            if "rate limit" in str(e).lower() and attempt < max_retries - 1:
                st.warning(f"Rate limit exceeded. Retrying... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(5)  # Wait for 5 seconds before retrying
            else:
                st.error(f"Error details: {e}")
                return None, None


# Function to execute SQL query on DataFrame
def execute_sql_query(df, query):
    conn = sqlite3.connect(":memory:")
    df.to_sql("data", conn, index=False, if_exists="replace")
    result_df = pd.read_sql_query(query, conn)
    conn.close()
    return result_df

# Function to plot data based on the suggested chart types
def plot_data(df, chart_types):
    for chart_type in chart_types:
        if len(df.columns) < 2:
            st.write(f"Chart type '{chart_type}' requires at least two columns in the data.")
            continue
        
        fig, ax = plt.subplots()
        if chart_type.lower() == 'bar chart':
            df.plot(kind='bar', x=df.columns[0], y=df.columns[1], ax=ax)
        elif chart_type.lower() == 'line chart':
            df.plot(kind='line', x=df.columns[0], y=df.columns[1], ax=ax)
        elif chart_type.lower() == 'pie chart':
            if df.shape[1] == 2 and df[df.columns[1]].sum() > 0:  # Check if the second column is suitable for pie chart
                df.set_index(df.columns[0], inplace=True)
                df.plot(kind='pie', y=df.columns[1], ax=ax, legend=False, autopct='%1.1f%%')
            else:
                st.write(f"Chart type '{chart_type}' not suitable for the data format.")
                continue
        elif chart_type.lower() == 'scatter plot' and df.shape[1] >= 2:
            df.plot(kind='scatter', x=df.columns[0], y=df.columns[1], ax=ax)
        else:
            st.write(f"Chart type '{chart_type}' not supported or data not suitable for this chart type.")
            continue
        plt.title(chart_type.capitalize())
        plt.xticks(fontsize=8, rotation=45)
        plt.yticks(fontsize=8)
        st.pyplot(fig)

# Title
st.title("Data Analysis with OpenAI")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.write(df)

    # User Input
    user_input = st.text_input("Enter your analysis request:")
    
    if user_input:
        # Generate SQL Query and Chart Types with OpenAI
        st.write("Generating SQL query and chart types with OpenAI...")
        sql_query, chart_types = generate_sql_query_and_chart(df, user_input)
        if sql_query and chart_types:
            st.write("Generated SQL Query:")
            st.code(sql_query)
            st.write(f"Suggested Chart Types: {', '.join(chart_types)}")
            
            try:
                # Execute SQL Query
                result_df = execute_sql_query(df, sql_query)
                st.write("Query Result DataFrame:")
                st.write(result_df)
                
                # Plot the query result data
                st.write("Plot of the query result data:")
                plot_data(result_df, chart_types)
            except Exception as e:
                st.write("Error in executing SQL query:")
                st.write(e)
else:
    st.write("Please upload a CSV file to see the data and plot.")
