import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://private-api.smrzr.io/v1/summarize?&num_sentences=5"


def summarise_text(payload):
    headers = {
        "Content-Type": "application/json",
        "api_token": os.getenv("BERT_SUMMARIZER_API_KEY"),
    }
    response = requests.post(API_URL, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        return response.json()["summary"].strip('"')
    else:
        print("Error:", response.status_code, response.text)
        return ""
