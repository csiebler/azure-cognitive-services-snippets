import os
import time
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('COMPUTER_VISION_ENDPOINT')

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

json = {
    "url": "https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/raw/master/samples/vision/images/make_things_happen.jpg"
}

params = {
    "language": "en",
    "pages": "1",
    "readingOrder": "natural"
}

r = requests.post(url=f"{endpoint}/vision/v3.2/read/analyze", params=params, headers=headers, json=json)

print(f"Status code: {r.status_code}")

if (r.status_code == 202):
    # Too lazy to query status of the job, so just wait - do not use this in your code :)
    time.sleep(5)
    r = requests.get(url=r.headers["Operation-Location"], headers=headers)
    print(f"Status code: {r.status_code}")
    print(f"Response body: {r.json()}")
