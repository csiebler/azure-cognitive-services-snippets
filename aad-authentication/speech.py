import os
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential
import azure.cognitiveservices.speech as speechsdk

load_dotenv()

resource_id = os.getenv('SPEECH_RESOURCE')
region = "westeurope" # update to your region

credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
access_token = credential.get_token("https://cognitiveservices.azure.com/")

authorization_token = "aad#" + resource_id + "#" + access_token.token

def from_mic():
    speech_config = speechsdk.SpeechConfig(auth_token=authorization_token, region=region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Say something...")
    result = speech_recognizer.recognize_once_async().get()
    
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

from_mic()