from flask import Flask, request, jsonify
import cv2
import numpy as np
import subprocess

app = Flask(__name__)

def detect_objects(image_path):
    cmd = f"./darknet detector test data/obj.data cfg/yolov7.cfg yolov7.weights {image_path} -dont_show -ext_output"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    image_path = "temp.jpg"
    file.save(image_path)
    
    detection_result = detect_objects(image_path)
    detections = parse_detection_output(detection_result)
    
    return jsonify({'detections': detections})

def parse_detection_output(output):
    detections = []
    lines = output.split('\n')
    for line in lines:
        if 'lesion' in line:
            parts = line.split()
            if len(parts) >= 8:
                x, y, w, h = float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5])
                conf = float(parts[1][:-1])
                detections.append({
                    'bbox': [x, y, w, h],
                    'confidence': conf
                })
    return detections

if __name__ == '__main__':
    app.run(debug=True)
