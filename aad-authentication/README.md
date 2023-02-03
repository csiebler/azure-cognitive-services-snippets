# Python code snippets for AAD (Azure Active Directory) authentication

If you are looking for a deeper explaination, have a look at this [blog post](https://clemenssiebler.com/azure-active-directory-aad-authentication-for-azure-cognitive-services/).

## Instructions

1. Create the desired Cognitive Service resource
1. Add your AAD user or your Managed Identity as a `Cognitive Services User` to the Cognitive Service resource
1. Enable `Custom Hostnames` (if not automatically activated) for your Cognitive Service resource
1. Copy `.env.example` to `.env` and update the details
1. Run the code
