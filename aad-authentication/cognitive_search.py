import os
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('COGNITIVE_SEARCH_ENDPOINT')
index_name = "transcription-index" # Update with your index name
query = "*"

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://search.azure.com/.default")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

r = requests.get(url=f"{endpoint}/indexes/{index_name}/docs?api-version=2021-04-30-Preview&search={query}", headers=headers)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
