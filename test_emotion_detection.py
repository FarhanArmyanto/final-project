from emotion_detection import emotion_detector

def test_emotion():
    result = emotion_detector("I am happy")
    assert result["dominant_emotion"] == "joy"
    print("Test passed!")

test_emotion()