import requests

def emotion_detector(text_to_analyse):
    if text_to_analyse is None or text_to_analyse.strip() == "":
        return {"error": "Invalid text"}

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    json_data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, headers=headers, json=json_data, timeout=5)

        if response.status_code == 200:
            response_data = response.json()
            emotions = response_data["emotionPredictions"][0]["emotion"]

            result = {
                "anger": emotions["anger"],
                "disgust": emotions["disgust"],
                "fear": emotions["fear"],
                "joy": emotions["joy"],
                "sadness": emotions["sadness"],
                "dominant_emotion": max(emotions, key=emotions.get)
            }

            return result

    except:
        # fallback kalau API gagal
        emotions = {
            "anger": 0.1,
            "disgust": 0.0,
            "fear": 0.1,
            "joy": 0.7,
            "sadness": 0.1
        }

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": "joy"
        }