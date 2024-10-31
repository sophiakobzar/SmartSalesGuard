import os
import pandas as pd
import re
import json
from openai import AzureOpenAI

# Ensure your environment variables are set correctly
ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-4-turbo-2024-04-09"  # Updated model name

# Load dataset
data = pd.read_csv('SuperStore Sales DataSet.csv')

# Preprocess data
data['Sales'] = data['Sales'].apply(lambda x: re.sub(r'[^0-9.]', '', str(x)))
data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')
data['Profit'] = pd.to_numeric(data['Profit'], errors='coerce')
data.dropna(subset=['Sales', 'Profit'], inplace=True)

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

# Messages for anomaly detection
MESSAGES_ANOMALY = [
    {"role": "system", "content": "You are a data scientist specializing in anomaly detection."},
    {"role": "user", "content": f"Detect any anomalies in the dataset: {data.head().to_json()}"}
]

# Messages for predictive forecasting
MESSAGES_FORECAST = [
    {"role": "system", "content": "You are a data scientist specializing in predictive forecasting."},
    {"role": "user", "content": f"Forecast future sales based on this dataset: {data.head().to_json()}"}
]

# Create completions for anomaly detection
completion_anomaly = client.chat.completions.create(
    model=MODEL_NAME,
    messages=MESSAGES_ANOMALY,
)

# Create completions for predictive forecasting
completion_forecast = client.chat.completions.create(
    model=MODEL_NAME,
    messages=MESSAGES_FORECAST,
)

# Convert the completion objects to dictionaries
completion_anomaly_dict = completion_anomaly.model_dump()
completion_forecast_dict = completion_forecast.model_dump()

# Save the JSON responses to files
with open('completion_anomaly_response.json', 'w') as json_file:
    json.dump(completion_anomaly_dict, json_file, indent=2)

with open('completion_forecast_response.json', 'w') as json_file:
    json.dump(completion_forecast_dict, json_file, indent=2)

print("JSON responses saved to completion_anomaly_response.json and completion_forecast_response.json")
