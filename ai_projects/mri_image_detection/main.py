import os
import numpy as np
import pickle
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Preparing data
input_dir = r'D:\my_work\personal_projects\ai_projects\mri_image_detection\archive\Testing'
categories = ['glioma', 'meningioma', 'notumor', 'pituitary']

data = []
labels = []

for category_idx, category in enumerate(categories):
    category_path = os.path.join(input_dir, category)

    for file in os.listdir(category_path):
        img_path = os.path.join(category_path, file)

        try:
            img = imread(img_path)  # Load image
            img = resize(img, (128, 128), anti_aliasing=True)  # Resize image
            
            # Convert grayscale to RGB if needed
            if len(img.shape) == 2:  # Grayscale image (H, W)
                img = np.stack([img] * 3, axis=-1)  # Convert to (H, W, 3)
            elif img.shape[2] == 4:  # If RGBA, convert to RGB
                img = img[:, :, :3]

            data.append(img)
            labels.append(category_idx)

        except Exception as e:
            print(f"Error loading {img_path}: {e}")

# Convert to NumPy arrays
data = np.array(data, dtype=np.float32)
labels = np.array(labels)

# Normalize pixel values (0-1 range)
data = data / 255.0

# Flatten images for SVM
data = data.reshape(data.shape[0], -1)  # (num_samples, 128*128*3)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels, random_state=42)

# Standardize Features for SVM
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train classifier (SVM with Grid Search)
classifier = SVC()
parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

# Best Model & Performance
best_estimator = grid_search.best_estimator_
y_prediction = best_estimator.predict(X_test)

score = accuracy_score(y_prediction, y_test)
print(f'{score * 100:.2f}% of samples were correctly classified')

# Save Model
pickle.dump(best_estimator, open('./model_svm.p', 'wb'))
pickle.dump(scaler, open('./scaler_svm.p', 'wb'))  # Save scaler for future use
