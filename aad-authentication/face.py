import os
import requests
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

endpoint = os.getenv('FACE_ENDPOINT', 'https://<your_face_hostname>.cognitiveservices.azure.com')

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

json = {
    "url": "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/faces.jpg"
}

r = requests.post(url=f"{endpoint}/face/v1.0/detect", headers=headers, json=json)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
