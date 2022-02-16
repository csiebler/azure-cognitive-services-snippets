import os
import requests
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

endpoint = os.getenv('PERSONALIZER_ENDPOINT', 'https://<your_personalizer_hostname>.cognitiveservices.azure.com')

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

r = requests.get(url=f"{endpoint}/personalizer/v1.0/configurations/service", headers=headers)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")

# Main code for actually using Personalizer needs to be written here
