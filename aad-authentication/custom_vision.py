import os
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('CUSTOM_VISION_PREDICTION_ENDPOINT')
project_id = "70377e33-aacd-43fd-bf2a-92c5501acb6f" # Replace with your project id
published_name = "Iteration1" # Replace with your published name

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

json = {
    "url": "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/CustomVision/ImageClassification/Images/Japanese_Cherry/japanese_cherry_1.jpg"
}

r = requests.post(url=f"{endpoint}/customvision/v3.1/prediction/{project_id}/classify/iterations/{published_name}/url/nostore", headers=headers, json=json)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
