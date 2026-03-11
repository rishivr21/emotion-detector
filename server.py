from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector App Running"

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze")

    if text is None or text.strip() == "":
        return "Invalid input! Please try again."

    result = emotion_detector(text)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)