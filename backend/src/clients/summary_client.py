import requests
import json

API_URL = "https://api.smrzr.io/v1/summarize?&num_sentences=5"

def summarise_text(payload):
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        return response.json()["summary"].strip('"')
    else:
        print("Error:", response.status_code, response.text)
        return ""

