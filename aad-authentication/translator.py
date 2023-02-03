import os
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('TRANSLATOR_ENDPOINT')

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

params = {
    "api-version": "3.0",
    "from": "en",
    "to": "de,nl",
    # "category": "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxx-GENERAL" # Add your custom model here
}

json = [
    {
        "text": "Translator is a cloud-based neural machine translation service that is part of the Azure Cognitive Services family of REST APIs. Translator can be used with any operating system and powers many Microsoft products and services used by thousands of businesses worldwide to perform language translation and other language-related operations. In this overview, you'll learn how Translator can enable you to build intelligent, multi-language solutions for your applications across all supported languages."
    }
]

r = requests.post(url=f"{endpoint}/translator/text/v3.0/translate", params=params, headers=headers, json=json)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
