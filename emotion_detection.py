"""Initial Watson NLP emotion detection exercise."""

import requests


def emotion_detector(text_to_analyze):
    """Return the Watson NLP response text for the supplied input."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    response = requests.post(
        url,
        headers=headers,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    return response.text
