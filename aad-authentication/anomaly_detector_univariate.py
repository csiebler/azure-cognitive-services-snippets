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
    "granularity": "daily",
    "series": [
      {
        "timestamp": "2018-03-01T00:00:00Z",
        "value": 32858923
      },
      {
        "timestamp": "2018-03-02T00:00:00Z",
        "value": 29615278
      },
      {
        "timestamp": "2018-03-03T00:00:00Z",
        "value": 22839355
      },
      {
        "timestamp": "2018-03-04T00:00:00Z",
        "value": 25948736
      },
      {
        "timestamp": "2018-03-05T00:00:00Z",
        "value": 34139159
      },
      {
        "timestamp": "2018-03-06T00:00:00Z",
        "value": 33843985
      },
      {
        "timestamp": "2018-03-07T00:00:00Z",
        "value": 33637661
      },
      {
        "timestamp": "2018-03-08T00:00:00Z",
        "value": 32627350
      },
      {
        "timestamp": "2018-03-09T00:00:00Z",
        "value": 29881076
      },
      {
        "timestamp": "2018-03-10T00:00:00Z",
        "value": 22681575
      },
      {
        "timestamp": "2018-03-11T00:00:00Z",
        "value": 24629393
      },
      {
        "timestamp": "2018-03-12T00:00:00Z",
        "value": 34010679
      },
      {
        "timestamp": "2018-03-13T00:00:00Z",
        "value": 33893888
      },
      {
        "timestamp": "2018-03-14T00:00:00Z",
        "value": 33760076
      },
      {
        "timestamp": "2018-03-15T00:00:00Z",
        "value": 33093515
      },
      {
        "timestamp": "2018-03-16T00:00:00Z",
        "value": 29945555
      },
      {
        "timestamp": "2018-03-17T00:00:00Z",
        "value": 22676212
      },
      {
        "timestamp": "2018-03-18T00:00:00Z",
        "value": 25262514
      },
      {
        "timestamp": "2018-03-19T00:00:00Z",
        "value": 33631649
      },
      {
        "timestamp": "2018-03-20T00:00:00Z",
        "value": 34468310
      },
      {
        "timestamp": "2018-03-21T00:00:00Z",
        "value": 34212281
      },
      {
        "timestamp": "2018-03-22T00:00:00Z",
        "value": 38144434
      },
      {
        "timestamp": "2018-03-23T00:00:00Z",
        "value": 34662949
      },
      {
        "timestamp": "2018-03-24T00:00:00Z",
        "value": 24623684
      },
      {
        "timestamp": "2018-03-25T00:00:00Z",
        "value": 26530491
      },
      {
        "timestamp": "2018-03-26T00:00:00Z",
        "value": 35445003
      },
      {
        "timestamp": "2018-03-27T00:00:00Z",
        "value": 34250789
      },
      {
        "timestamp": "2018-03-28T00:00:00Z",
        "value": 33423012
      },
      {
        "timestamp": "2018-03-29T00:00:00Z",
        "value": 30744783
      },
      {
        "timestamp": "2018-03-30T00:00:00Z",
        "value": 25825128
      },
      {
        "timestamp": "2018-03-31T00:00:00Z",
        "value": 21244209
      },
      {
        "timestamp": "2018-04-01T00:00:00Z",
        "value": 22576956
      },
      {
        "timestamp": "2018-04-02T00:00:00Z",
        "value": 31957221
      },
      {
        "timestamp": "2018-04-03T00:00:00Z",
        "value": 33841228
      },
      {
        "timestamp": "2018-04-04T00:00:00Z",
        "value": 33554483
      }
    ]
  }

r = requests.post(url=f"{endpoint}/anomalydetector/v1.0/timeseries/entire/detect", headers=headers, json=json)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
