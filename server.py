from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion():
    text = request.args.get('textToAnalyze')

    if not text:
        return "Invalid input", 400

    result = emotion_detector(text)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
