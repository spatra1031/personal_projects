Movie Data Analysis & Prediction
This project focuses on analyzing a movie dataset to uncover key insights about movie attributes and their relationships. It also involves training a machine learning model to predict a movie's revenue based on various features. The dataset contains details about over 5000 movies, including information about the movie's budget, revenue, genres, production companies, and more.

Table of Contents
Project Overview

Data Overview

Project Setup

Exploratory Data Analysis (EDA)

Feature Engineering

Modeling

Results & Evaluation

Conclusion

Future Work

Screenshots

Project Overview
In this project, we analyze a movie dataset to explore various patterns, detect correlations, and build a predictive model to estimate movie revenues. The dataset contains two primary files: one with movie data (tmdb_5000_movies.csv) and one with credits data (tmdb_5000_credits.csv).

We combine these datasets and perform several key data cleaning, preprocessing, and feature engineering steps to prepare the data for further analysis and machine learning.

Key Objectives:
Analyze movie data to identify trends and insights (e.g., most popular genres, top directors, etc.).

Investigate the relationship between different variables, such as budget, revenue, and profitability.

Build a machine learning model (Linear Regression) to predict movie revenue based on available features.

Data Overview
The dataset used in this project contains information about movies released between 1960 and 2020. The columns in the dataset include:

id: Unique identifier for each movie.

title: Movie title.

genres: Genres associated with the movie.

budget: Movie's production budget.

revenue: Movie's box office revenue.

release_date: Date the movie was released.

runtime: Duration of the movie in minutes.

vote_average: Average rating based on user votes.

vote_count: Total number of votes.

original_language: Language of the movie.

director: Movie's director(s).

cast: Top cast members of the movie.

Project Setup
To run this project locally, ensure you have the following dependencies installed:

Install Dependencies
You can install the necessary libraries by running the following command:

bash
Copy
Edit
pip install -r requirements.txt
Folder Structure
bash
Copy
Edit
/project-root
│
├── /data
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│
├── /notebooks
│   ├── movie_analysis.ipynb
│
├── requirements.txt
├── README.md
Required Libraries:
pandas

numpy

matplotlib

seaborn

scikit-learn

ast

datetime

Exploratory Data Analysis (EDA)
In this section, we perform exploratory data analysis to better understand the dataset.

Descriptive Statistics
We begin by generating descriptive statistics for the numerical columns.

Code:
python
Copy
Edit
merged_df.describe()
Data Distribution
We visualize the distribution of the budget and revenue columns with histograms and boxplots to identify skewness and outliers.

Code:
python
Copy
Edit
sns.boxplot(x=merged_df['revenue'])
Missing Data Visualization
We visualize missing data using a heatmap to identify any columns with significant missing values.

Code:
python
Copy
Edit
sns.heatmap(merged_df.isnull(), cbar=False, cmap='viridis')
Correlation Matrix
A correlation matrix is computed for numerical columns to uncover relationships between key attributes like budget, revenue, and vote_average.

Code:
python
Copy
Edit
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
Categorical Features Analysis
We plot the top 10 genres and directors to understand the most common categories.

Code:
python
Copy
Edit
genre_counts.plot(kind='barh')
Screenshot 1: Distribution of Movie Genres
You can add a screenshot of the bar plot showing the top 10 genres here.

Feature Engineering
In this section, we create new features to enhance the dataset's predictive power.

Profit and ROI
We calculate the profit (revenue - budget) and the ROI (return on investment) for each movie.

Code:
python
Copy
Edit
merged_df['profit'] = merged_df['revenue'] - merged_df['budget']
merged_df['roi'] = merged_df.apply(lambda row: (row['revenue'] - row['budget']) / row['budget'] if row['budget'] != 0 else 0, axis=1)
Log Transformations
To handle skewed distributions, we apply log transformations to the budget and revenue columns.

Code:
python
Copy
Edit
merged_df['log_revenue'] = merged_df['revenue'].apply(lambda x: np.log1p(x))
merged_df['log_budget'] = merged_df['budget'].apply(lambda x: np.log1p(x))
Modeling
We train a Linear Regression model to predict the revenue based on various features.

Data Splitting
We split the dataset into training and testing sets.

Code:
python
Copy
Edit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
Model Training
We train a Linear Regression model and evaluate its performance using Mean Squared Error (MSE) and R² Score.

Code:
python
Copy
Edit
model.fit(X_train, y_train)
Model Evaluation
We evaluate the model's predictions against actual values.

Code:
python
Copy
Edit
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
Screenshot 2: Predicted vs Actual Revenue
You can add a screenshot of the scatter plot comparing predicted vs actual revenue here.

Results & Evaluation
After training the model, we evaluate its performance on unseen test data. The model's accuracy is measured using metrics such as Mean Squared Error (MSE) and R² Score.

Model Evaluation Results:
MSE: [Insert MSE Value]

R² Score: [Insert R² Score Value]

Conclusion
The analysis revealed several key insights about the movie dataset:

[Include any significant insights like trends in budget/revenue, popular genres, etc.]

The Linear Regression model performed well, although there is room for improvement by tuning hyperparameters or testing other machine learning algorithms.

Future Work
Hyperparameter Tuning: We can improve the model's performance by tuning hyperparameters.

Alternative Models: Testing more advanced models such as Random Forests or Gradient Boosting could lead to better predictions.

Further EDA: Additional analysis on other features, such as runtime, could uncover more patterns.

Real-time Prediction: Build a web-based tool to predict movie revenues based on user input.

Screenshots
Screenshot 1: Distribution of Movie Genres Add a screenshot of the bar plot showing the top 10 genres here.

Screenshot 2: Predicted vs Actual Revenue Add a screenshot of the scatter plot comparing predicted vs actual revenue here.

