import constants, requests


def emotion_detector(text_to_analyse):
    """
    This method analyse emotion in a passed text

    Parameters
    ----------
    param1 : str
        Text to analyse a string value.

    Returns
    -------
    str
        Response of the emotion analysis

    Raises
    ------
    ValueError
        If param1 is not a string of >0 length.
    """
    if not isinstance(text_to_analyse, str) or len(text_to_analyse) <= 0:
        raise ValueError("Incorrect parameter passed to emotion_detector. Use Valid string of >0 length")
    
    request_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(constants.WATSON_URL, json=request_json, headers=constants.MODEL_HEADER)

    return response.text
