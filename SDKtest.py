import os
from openai import AzureOpenAI
import json

# Ensure your environment variables are set correctly
ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
API_KEY = os.getenv('AZURE_OPENAI_API_KEY')

API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-4-turbo-2024-04-09"  # Updated model name

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020.",
    },
    {"role": "user", "content": "Where was it played?"},
]

completion = client.chat.completions.create(
    model=MODEL_NAME,
    messages=MESSAGES,
)

# Convert the completion object to a dictionary
completion_dict = completion.model_dump()

# Save the JSON response to a file
with open('completion_response.json', 'w') as json_file:
    json.dump(completion_dict, json_file, indent=2)

print("JSON response saved to completion_response.json")
