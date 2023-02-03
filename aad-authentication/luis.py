import os
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('LUIS_ENDPOINT')
model_id = "beadbdb2-cde2-49a5-8780-4989ae913000" # Update with your model id
slot = "production"

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

params = {
    "verbose": "true",
    "show-all-intents": "true",
    "log": "true",
    "query": "what is the time?"
}

r = requests.get(url=f"{endpoint}/luis/prediction/v3.0/apps/{model_id}/slots/{slot}/predict", params=params, headers=headers)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
