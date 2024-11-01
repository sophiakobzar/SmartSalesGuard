from flask import Flask, request, jsonify, send_from_directory
import os
import pandas as pd
import re
import json
from openai import AzureOpenAI

app = Flask(__name__, static_folder='')

def preprocess_data():
    data = pd.read_csv('SuperStore Sales DataSet.csv')
    data['Sales'] = data['Sales'].apply(lambda x: re.sub(r'[^0-9.]', '', str(x)))
    data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')
    data['Profit'] = pd.to_numeric(data['Profit'], errors='coerce')
    data.dropna(subset=['Sales', 'Profit'], inplace=True)
    return data

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    content = request.json
    api_key = content.get('apiKey')
    endpoint = content.get('endpoint')
    analysis_type = content.get('analysisType')
    
    print(f"API Key: {api_key}")
    print(f"Endpoint: {endpoint}")
    print(f"Analysis Type: {analysis_type}")
    
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version="2024-02-01",
    )
    
    data = preprocess_data()
    
    if analysis_type == "anomaly":
        messages = [
            {"role": "system", "content": "You are a data scientist specializing in anomaly detection."},
            {"role": "user", "content": f"Detect any anomalies in the dataset: {data.head().to_json()}"}
        ]
    elif analysis_type == "forecast":
        messages = [
            {"role": "system", "content": "You are a data scientist specializing in predictive forecasting."},
            {"role": "user", "content": f"Forecast future sales based on this dataset: {data.head().to_json()}"}
        ]
    else:
        return jsonify({"error": "Invalid analysis type specified"}), 400
    
    try:
        completion = client.chat.completions.create(model="gpt-4-turbo-2024-04-09", messages=messages)
        response_content = completion.model_dump()['choices'][0]['message']['content']
        print(f"Response Content: {response_content}")
        return jsonify({"content": response_content})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
