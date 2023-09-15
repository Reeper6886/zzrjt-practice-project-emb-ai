''' Imports
'''
import json
import requests

def sentiment_analyzer(text_to_analyze):
    """
    Analyze the sentiment of the given text.

    Args:
        text_to_analyze (str): The text to be analyzed for sentiment.

    Returns:
        dict: A dictionary containing the sentiment label and score.
    """
    url = (
        'https://sn-watson-sentiment-bert.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )

    myobj = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        formatted_response = json.loads(response.text)

        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        else:
            label = None
            score = None
    except requests.exceptions.RequestException:
        label = None
        score = None

    return {'label': label, 'score': score}
