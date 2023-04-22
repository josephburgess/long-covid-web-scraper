"""
Simple client to interact with a summarization API - BERT extractive summarizer.
"""
import json
import requests

API_URL = "https://api.smrzr.io/v1/summarize?&num_sentences=5"


def summarise_text(payload):
    """
    Summarize text using the BERT extractive summarizer.
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        API_URL, data=json.dumps(payload), headers=headers, timeout=10
    )
    if response.status_code == 200:
        return response.json()["summary"].strip('"')

    print("Error:", response.status_code, response.text)
    return ""
