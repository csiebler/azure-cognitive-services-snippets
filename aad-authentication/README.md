# Python code snippets for AAD (Azure Active Directory) authentication

## Instructions

1. Create the desired Cognitive Service resource
1. Add your AAD user or your Managed Identity as a `Cognitive Services User` to the Cognitive Service resource
1. Enable `Custom Hostnames` (if not automatically activated) for your Cognitive Service resource
1. Export hostname/resource id to `env` or update in code (see in `.py` files)
1. Run the code

Linux/macOS:
```
export TRANSLATOR_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export ANOMALY_DETECTOR_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export LANGUAGE_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export COMPUTER_VISION_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export CONTENT_MODERATOR_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export FORM_RECOGNIZER_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export PERSONALIZER_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export COGNITIVE_SEARCH_ENDPOINT=https://<replace>.search.windows.net
export CUSTOM_VISION_PREDICTION_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export FACE_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export LUIS_ENDPOINT=https://<replace>.cognitiveservices.azure.com
export SPEECH_RESOURCE=/subscriptions/<replace>/resourceGroups/<replace>/providers/Microsoft.CognitiveServices/accounts/<replace>
```

Windows:
```
$env:TRANSLATOR_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:ANOMALY_DETECTOR_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:LANGUAGE_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:COMPUTER_VISION_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:CONTENT_MODERATOR_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:FORM_RECOGNIZER_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:PERSONALIZER_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:COGNITIVE_SEARCH_ENDPOINT = "https://<replace>.search.windows.net"
$env:CUSTOM_VISION_PREDICTION_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:FACE_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:LUIS_ENDPOINT = "https://<replace>.cognitiveservices.azure.com"
$env:SPEECH_RESOURCE = "/subscriptions/<replace>/resourceGroups/<replace>/providers/Microsoft.CognitiveServices/accounts/<replace>"
```