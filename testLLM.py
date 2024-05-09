import requests
import extraction
import os

os.environ['CURL_CA_BUNDLE'] = ''

#Prefedined API token and url, using gpt2-xl
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/gpt2-xl"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def llmInput(path):
    data = query({"inputs": extraction.extract(path).replace("\n", "") + "The company is partcularly prone or resilient " +
                            "to interest rate fluctuations as",
                  "parameters": {"max_length": 500, "max_new_tokens": 250, "return_full_text": False},
                  "options": {"wait_for_model": True}})
    return data
