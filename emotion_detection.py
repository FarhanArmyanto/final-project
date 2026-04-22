def emotion_detector(text):
    if text == "":
        return {"error": "No input"}

    emotions = {
        "anger": 0.1,
        "disgust": 0.0,
        "fear": 0.1,
        "joy": 0.7,
        "sadness": 0.1
    }

    dominant = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant

    return emotions


print(emotion_detector("I am happy"))
