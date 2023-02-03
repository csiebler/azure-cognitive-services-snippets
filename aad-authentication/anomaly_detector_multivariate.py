import os
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('ANOMALY_DETECTOR_ENDPOINT')

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

json = {
    "slidingWindow": 200,
    "alignPolicy": {
        "alignMode": "Outer",
        "fillNAMethod": "Linear", 
        "paddingValue": 0
    },
    "source": "https://aka.ms/AnomalyDetector/MVADSampleData", 
    "startTime": "2021-01-01T00:00:00Z", 
    "endTime": "2021-01-02T12:00:00Z", 
    "displayName": "Test Model"
}

r = requests.post(url=f"{endpoint}/anomalydetector/v1.1-preview.1/multivariate/models", headers=headers, json=json)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")

r = requests.get(url=f"{endpoint}/anomalydetector/v1.1-preview.1/multivariate/models", headers=headers)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
