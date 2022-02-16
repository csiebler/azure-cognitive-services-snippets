import os
import requests
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

endpoint = os.getenv('CONTENT_MODERATOR_ENDPOINT', 'https://<your_content_moderator_hostname>.cognitiveservices.azure.com')

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
  "Content-Type": "text/plain",
  "Authorization": f"Bearer {access_token.token}"
}

text = "This is just a simple text."

r = requests.post(url=f"{endpoint}/contentmoderator/moderate/v1.0/ProcessText/DetectLanguage", headers=headers, data=text.encode('utf-8'))

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
