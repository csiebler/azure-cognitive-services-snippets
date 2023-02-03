import os
import time
import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential

load_dotenv()

endpoint = os.getenv('LANGUAGE_ENDPOINT')

# Define strategy which potential authentication methods should be tried to gain an access token
credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token.token}"
}

json = {
  "analysisInput": {
    "documents": [
      {
        "language": "en",
        "id": "1",
        "text": "Translator is a cloud-based neural machine translation service that is part of the Azure Cognitive Services family of REST APIs. Translator can be used with any operating system and powers many Microsoft products and services used by thousands of businesses worldwide to perform language translation and other language-related operations. In this overview, you'll learn how Translator can enable you to build intelligent, multi-language solutions for your applications across all supported languages."
      },
      {
        "language": "de",
        "id": "2",
        "text": "Der Übersetzer ist ein cloudbasierter Dienst für neuronale maschinelle Übersetzung, der zur Azure Cognitive Services-Familie der REST-APIs gehört. Der Übersetzer kann mit jedem Betriebssystem verwendet werden und unterstützt viele Microsoft-Produkte und -Dienste, die von Tausenden von Unternehmen weltweit verwendet werden, um Sprachübersetzungen und andere sprachbezogene Vorgänge durchzuführen. In dieser Übersicht erfahren Sie, wie Sie mit dem Übersetzer intelligente, mehrsprachige Lösungen für Ihre Anwendungen in allen unterstützten Sprachen erstellen können."
      }
    ]
  },
  "tasks": {
    "extractiveSummarizationTasks": [
      {
        "parameters": {
          "model-version": "latest",
          "sentenceCount": 2,
          "sortBy": "Rank"
        }
      }
    ]
  }
}

r = requests.post(url=f"{endpoint}/text/analytics/v3.2-preview.1/analyze", headers=headers, json=json)

print(f"Status code: {r.status_code}")

if (r.status_code == 202):
    # Too lazy to query status of the job, so just wait - do not use this in your code :)
    time.sleep(5)
    r = requests.get(url=r.headers["Operation-Location"], headers=headers)
    print(f"Status code: {r.status_code}")
    print(f"Response body: {r.json()}")
