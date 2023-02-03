import os
import time
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('OPENAI_ENDPOINT')
deployment = "text-davinci-003"

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

prompt = """Airport code extractor:

Text: "I want to fly form Los Angeles to Miami."
Airport codes: LAX, MIA
##
Text: "I want to fly form New York, JFK to San Francisco."
Airport codes: JFK, SFO
##
Text: "I want to fly from Orlando to Boston"
Airport codes:"""

payload = {
    "prompt": prompt,
    "max_tokens": 50,
    "temperature": 1,
    "top_p": 1,
    "echo": False,
    "n": 1,
    "stop": ["##"],
    "frequency_penalty": 1,
    "presence_penalty" : 1.5
}

params = {
  'api-version': '2022-12-01'
}
r = requests.post(url=f"{endpoint}/openai/deployments/{deployment}/completions", headers=headers, params=params, json=payload)

print(f"Status code: {r.status_code}")
print(f"Response body: {r.json()}")
