# MRI Brain Tumor Detection AI
A deep learning-based web application that detects brain tumors from MRI scans. This project utilizes a Convolutional Neural Network (CNN) trained to classify MRI images into four categories: glioma, meningioma, no tumor, and pituitary tumor. The model is integrated into a Streamlit web app for easy and interactive diagnosis.

## Key Features
✔ Deep Learning-Based MRI Tumor Classification
✔ User-Friendly Streamlit Web Interface
✔ Automated Image Preprocessing & Normalization
✔ Interactive Upload & Real-Time Prediction

### 1. Project Overview
This project leverages computer vision and deep learning to classify brain tumors from MRI scans. The model is trained on a labeled MRI dataset and deployed as a real-time prediction web application.

### 2. Dataset & Preprocessing
Dataset stored in archive/Training and archive/Testing folders
Images resized to 128×128 pixels for uniform processing
Data augmentation applied to enhance model generalization
Data Augmentation Techniques
Rotation (20°)
Width & Height Shifts
Horizontal Flipping
Pixel Value Normalization

## 3. Model Architecture
A Convolutional Neural Network (CNN) is used to classify MRI images into four tumor types.

### CNN Architecture
3 Convolutional Layers with ReLU activation
MaxPooling for down-sampling
Fully Connected Layer (Dense) for final classification

### Compilation & Training
Optimizer: Adam
Loss Function: Categorical Cross-Entropy
Metric: Accuracy

## 4. Model Training & Evaluation
Trained for 10 epochs (adjustable based on performance)
Model Checkpoint to save the best performing model
Accuracy Graph plotted to visualize model performance

Example Screenshot - Training Accuracy Graph:

## 5. Web App Deployment with Streamlit
The trained model is deployed using Streamlit, allowing users to upload an MRI image and get real-time predictions.

Steps in Web App Workflow
User uploads an MRI image (.jpg, .png, .jpeg).
Image is preprocessed (resized to 128×128 and normalized).
Model makes a prediction and classifies the image.
Confidence score displayed along with the predicted class.

Example Screenshot - Web App Prediction:

## 6. Real-World Impact
This project provides a non-invasive, AI-assisted diagnosis tool for early brain tumor detection.

🔹 Healthcare Benefits
Speeds up diagnosis and assists radiologists
Reduces human error in tumor classification
Enables remote MRI analysis through a web interface
🔹 Potential Use Cases
Hospitals & Clinics: AI-assisted radiology for brain scans
Medical Research: Identifying patterns in tumor progression
Telemedicine: Remote consultations using AI-driven reports

## 7. Future Enhancements
🔹 Improve Model Accuracy using a larger dataset & deeper CNN model
🔹 Mobile App Integration for on-the-go MRI analysis
🔹 Multi-Class Tumor Detection with additional categories