# VSCode REST Client snippets

## Instructions

1. Use VSCode with the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension
1. Create a `Multi-Service Cognitive Service` resource in Azure ([see here](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account?tabs=multiservice%2Cwindows))
1. (Optional) Create a `Translator` resource with `S1` pricing tier in Azure ([see here](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-how-to-signup)) - this is only required for Document Translation
1. Update your VSCode `settings.json` and add this section:
    ```json
        "rest-client.environmentVariables": {
        "$shared": {
            "cognitive_services_endpoint": "https://<your resource name>.cognitiveservices.azure.com",
            "cognitive_services_key": "<Your Cognitive Service resource key>",
            "translator_endpoint": "https://<your Translator resource name>.cognitiveservices.azure.com", # optional, only required when using Translator
            "translator_key": "<your Translator resource key>", # optional, only required when using Translator
            "translator_region": "<your Translator resource location>", # optional, e.g. westeurope - only required when using Translator
            "search_instance_name": "<name of your search instance>", # optional, only required when using Azure Cognitive Search
            "search_query_key": "<search instance query key>" # optional, only required when using Azure Cognitive Search
        }
    ```
1. Open one of the `*.http` files and run the requests inside VSCode