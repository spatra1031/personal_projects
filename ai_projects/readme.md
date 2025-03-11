# AI Projects 🚀🧠

Welcome to my AI projects repository! This collection showcases my work in computer vision, AI-powered dashboards, and medical imaging. Each project solves real-world problems using advanced AI techniques, integrating machine learning, deep learning, and data visualization.

## Projects Overview

### 1️⃣ AI-Powered Parking Lot Monitoring System 🚗
📌 Directory: ai_projects/parking_lot_monitoring
🔗 Technologies: Python, OpenCV, PostgreSQL, ArcGIS, Computer Vision

#### Overview
This system automates parking lot monitoring using computer vision and integrates real-time data with ArcGIS for spatial visualization. It detects and tracks 396 parking spots, determining their availability using a trained AI model.

#### Key Features:
✅ Real-time Video Processing – Uses OpenCV to analyze live CCTV footage.
✅ AI-Based Parking Detection – Classifies each spot as Empty or Occupied.
✅ Database Integration – Updates parking status in PostgreSQL and CSV files.
✅ GIS Integration – Uses ArcGIS to visualize parking availability on a map.
✅ Web App Interface – Displays real-time parking information on an external screen.

#### How It Works:
Detects parking spots from a masked image using cv2.connectedComponentsWithStats.
Classifies spots based on pixel differences between frames.
Stores results in a PostgreSQL database and updates a CSV file.
Visualizes data using ArcGIS Feature Layers.
📌 Future Enhancements:
🔹 Deploy as a fully cloud-based GIS web app.
🔹 Integrate license plate recognition for advanced analytics.

### 2️⃣ AI-Powered Data Analysis Dashboard 📊
📌 Directory: ai_projects/ai_dashboard
🔗 Technologies: Python, Streamlit, OpenAI API, SQLite, Pandas, Matplotlib

#### Overview
An AI-driven interactive data analytics dashboard that allows users to upload CSV files, query data using natural language, and generate insights. The app uses OpenAI’s GPT model to generate SQL queries dynamically and suggest the best chart types for visualization.

#### Key Features:
✅ Natural Language Querying – Converts user input into SQL queries using OpenAI.
✅ Automated Chart Suggestions – Generates bar, line, pie, or scatter plots dynamically.
✅ Real-time Data Execution – Runs SQL queries on uploaded datasets using SQLite.
✅ Interactive UI – Powered by Streamlit for a seamless user experience.

#### How It Works:
User uploads a CSV file.
Enters a question like: "Show me sales trends over time."
OpenAI generates an SQL query.
SQLite executes the query.
Results are visualized in an appropriate chart.
📌 Future Enhancements:
🔹 Implement multi-dataset querying.
🔹 Add predictive analytics using AI models.

### 3️⃣ MRI Brain Tumor Detection 🧠🏥
📌 Directory: ai_projects/mri_image_detection
🔗 Technologies: Python, TensorFlow, Streamlit, OpenCV, PIL

#### Overview
This AI-powered tool analyzes MRI scans to detect brain tumors. It is designed to assist radiologists by providing an automated, fast, and accurate diagnosis of brain tumors.

#### Key Features:
✅ Deep Learning Model – Trained using CNNs (Convolutional Neural Networks).
✅ Tumor Classification – Detects glioma, meningioma, pituitary tumor, or no tumor.
✅ User-Friendly Web App – Built with Streamlit for easy image uploads and predictions.
✅ Real-Time Confidence Scores – Provides model confidence levels for each prediction.

#### How It Works:
User uploads an MRI scan.
Image is preprocessed (resized, normalized, and batch dimension added).
CNN model predicts tumor type with a confidence score.
Results are displayed in an interactive Streamlit UI.
📌 Future Enhancements:
🔹 Improve accuracy with transfer learning on larger MRI datasets.
🔹 Deploy as a cloud-based medical AI service.