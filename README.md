# Emotion Detector

This project is an AI-based Emotion Detection web application developed using Python and Flask.  
It detects emotions in a given text using the IBM Watson NLP API.

## Project Description
The application takes a sentence as input and analyzes it to detect emotions such as joy, sadness, anger, fear, and disgust. It then identifies the dominant emotion in the text.

## Features
- Detects emotions from user text
- Shows the dominant emotion
- Web interface using Flask
- Unit testing for validation
- Error handling for invalid inputs

## Technologies Used
- Python
- Flask
- IBM Watson NLP
- Requests library

## Project Structure
emotion-detector
│
├── EmotionDetection
│ ├── init.py
│ └── emotion_detection.py

├── server.py
├── test_emotion_detection.py
└── README.md

## How to Run the Project

1. Install required libraries
2. pip install flask requests


2. Run the server

python server.py


3. Open browser

http://127.0.0.1:5000/emotionDetector?textToAnalyze=I%20am%20happy


## Author
Rishikant Verma  
Student at Trident Academy of Technology

GitHub: https://github.com/rishivr21
