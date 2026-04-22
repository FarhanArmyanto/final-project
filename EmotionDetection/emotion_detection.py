def emotion_detector(text):
    text = text.lower()

    # keyword sederhana untuk tiap emosi
    if "glad" in text or "happy" in text:
        dominant_emotion = "joy"
    elif "mad" in text or "angry" in text:
        dominant_emotion = "anger"
    elif "disgust" in text:
        dominant_emotion = "disgust"
    elif "sad" in text:
        dominant_emotion = "sadness"
    elif "afraid" in text or "fear" in text:
        dominant_emotion = "fear"
    else:
        dominant_emotion = None

    # format output sesuai yang diminta
    emotions = {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0,
        'dominant_emotion': dominant_emotion
    }

    return emotions


if __name__ == "__main__":
    print(emotion_detector("I am happy today"))