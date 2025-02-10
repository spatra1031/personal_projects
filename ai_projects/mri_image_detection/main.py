import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import ModelCheckpoint

# Define dataset path
dataset_path = r"D:\my_work\personal_projects\ai_projects\mri_image_detection\archive/"

# Image parameters
img_size = 128  # Resize all images to 128x128
batch_size = 32  # Number of images fed into CNN at once

# Data Augmentation to improve model performance
train_datagen = ImageDataGenerator(
    rescale=1./255,  # Normalize pixel values (0-255 → 0-1)
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2  # 20% of data is for validation
)

# Load Training Data
train_generator = train_datagen.flow_from_directory(
    os.path.join(dataset_path, "Training"),
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

# Load Validation Data
val_generator = train_datagen.flow_from_directory(
    os.path.join(dataset_path, "Training"),
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Get class labels
class_names = list(train_generator.class_indices.keys())
print("Class labels:", class_names)

# Define the CNN model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(img_size, img_size, 3)),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')  # 4 classes: glioma, meningioma, no tumor, pituitary
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Model summary
model.summary()

# Set up Model Checkpoint
checkpoint = ModelCheckpoint("mri_brain_tumor_model.h5", save_best_only=True, verbose=1)

# Train the CNN
epochs = 10  # Adjust based on performance
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=epochs,
    callbacks=[checkpoint]  # Save the best model during training
)

# Plot training history
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Final model save
try:
    model.save("mri_brain_tumor_model.h5")
    print("Model saved successfully!")
except Exception as e:
    print(f"Error saving model: {e}")
