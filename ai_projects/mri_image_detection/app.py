import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
MODEL_PATH = "mri_brain_tumor_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels
class_names = ["glioma", "meningioma", "no tumor", "pituitary"]

# Function to preprocess image
def preprocess_image(image):
    # Convert RGBA images (with 4 channels) to RGB (3 channels)
    if image.mode == "RGBA":
        image = image.convert("RGB")

    image = image.resize((128, 128))  # Resize to match model input size
    image = np.array(image) / 255.0   # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit UI
st.title("MRI Brain Tumor Detection")
st.write("Upload an MRI image to detect the type of tumor.")

uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)
    
    # Preprocess and predict
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)
    
    st.write(f"### Prediction: {predicted_class}")
    st.write(f"### Confidence: {confidence:.2f}")
