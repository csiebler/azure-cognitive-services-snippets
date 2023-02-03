import os
import time
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('FORM_RECOGNIZER_ENDPOINT')

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

json = {
    "source": "https://github.com/Azure-Samples/cognitive-services-REST-api-samples/raw/master/curl/form-recognizer/Invoice-6.pdf"
}

r = requests.post(url=f"{endpoint}/formrecognizer/v2.1/prebuilt/invoice/analyze", headers=headers, json=json)

print(f"Status code: {r.status_code}")

if (r.status_code == 202):
    # Too lazy to query status of the job, so just wait - do not use this in your code :)
    time.sleep(5)
    r = requests.get(url=r.headers["Operation-Location"], headers=headers)
    print(f"Status code: {r.status_code}")
    print(f"Response body: {r.json()}")
