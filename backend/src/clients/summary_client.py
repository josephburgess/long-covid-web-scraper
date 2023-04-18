import requests
import json

API_URL = "https://api.smrzr.io/v1/summarize?&num_sentences=5"


def summariseText(payload):
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, data=json.dumps(payload), headers=headers)
    return response.json()["summary"].strip('"')
