import requests

def emotion_detector(text_to_analyse):
    
    if not text_to_analyse:
        return {"error": "Invalid input"}

    url = "https://api.example.com/emotion"
    response = {
        "anger": 0.1,
        "disgust": 0.0,
        "fear": 0.2,
        "joy": 0.6,
        "sadness": 0.1
    }

    dominant_emotion = max(response, key=response.get)

    return {
        "anger": response["anger"],
        "disgust": response["disgust"],
        "fear": response["fear"],
        "joy": response["joy"],
        "sadness": response["sadness"],
        "dominant_emotion": dominant_emotion
    }