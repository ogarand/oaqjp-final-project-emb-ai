import constants, requests, json


def emotion_detector(text_to_analyse):
    request_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(constants.WATSON_URL, json=request_json, headers=constants.MODEL_HEADER)
    parsed_response = {}

    if response.status_code == 400:
        parsed_response = {
            "anger": "None",
            "disgust": "None",
            "fear": "None",
            "joy": "None",
            "sadness": "None",
            "dominant_emotion" : "None"
        }
    else:
        response_dictionary = json.loads(response.text)
        if not response_dictionary.get('emotionPredictions'):
            return {}

        emotion_predictions = response_dictionary['emotionPredictions'][0]['emotion']

        parsed_response = {
            "anger": emotion_predictions['anger'],
            "disgust": emotion_predictions['disgust'],
            "fear": emotion_predictions['fear'],
            "joy": emotion_predictions['joy'],
            "sadness": emotion_predictions['sadness'],
        }

        # find the dominant emotion
        dominant_emotion, _ = get_max_value(parsed_response)
        parsed_response["dominant_emotion"] = dominant_emotion

    return parsed_response


def get_max_value(data: dict) -> tuple[str, float]:
    """
    Return the (label, value) pair with the greatest value from a dictionary.
    """
    if not data:
        raise ValueError("Dictionary is empty")
    
    return max(data.items(), key=lambda item: item[1])


