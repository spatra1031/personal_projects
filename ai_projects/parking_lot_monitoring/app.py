from flask import Flask, request, jsonify, send_file, render_template
from processing.frame_extraction import extract_frames, preprocess_frame
from detection.detect_objects import load_detection_model, detect_objects
from detection.identify_spaces import identify_parking_spaces
from detection.classify_spaces import classify_spaces
from visualization.create_model import create_2d_model
import cv2
import numpy as np
import os

app = Flask(__name__, static_folder='static')
model = load_detection_model()  # Load the YOLOv8 model when the app starts

@app.route('/process_video', methods=['POST'])
def process_video():
    video_file = 'parking_lot.mp4'  # Update the path to the video file
    frames = extract_frames(video_file)  # Extract frames from the video
    preprocessed_frames = [preprocess_frame(frame) for frame in frames]  # Preprocess each frame
    parking_spaces = identify_parking_spaces(preprocessed_frames[0])  # Identify parking spaces (using the first frame as an example)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (preprocessed_frames[0].shape[1], preprocessed_frames[0].shape[0]))

    for i, frame in enumerate(preprocessed_frames):
        detections = detect_objects(frame, model)  # Detect objects in each frame
        classified_spaces = classify_spaces(parking_spaces, detections)  # Classify spaces as empty or occupied
        for space in classified_spaces:
            x, y, w, h, occupied = space
            color = (0, 255, 0) if not occupied else (0, 165, 255)  # Green for empty, Orange for occupied
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        
        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    out.release()

    model_image_path = create_2d_model(classified_spaces)  # Create a 2D model visualization of the parking lot

    return jsonify({'classified_spaces': classified_spaces, 'model_image': model_image_path, 'video_output': 'output.avi'})  # Return the results as JSON

@app.route('/download_video')
def download_video():
    return send_file('output.avi', as_attachment=True)

@app.route('/view_model')
def view_model():
    return render_template('view_model.html', model_image='model_image.png')

if __name__ == '__main__':
    app.run(debug=True)
