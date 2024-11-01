# SmartSalesGuard

## Project Overview
SmartSalesGuard is a project aimed at detecting anomalies in sales data to identify unusual patterns or potential fraud for an online Super Store. This project leverages Microsoft Fabric and Azure OpenAI services to process and analyze data, providing real-time insights and anomaly detection.

## Features
- **Data Collection**: Import sales data from Kaggle into Azure Database for PostgreSQL.
- **Data Preprocessing**: Clean and prepare data for machine learning.
- **Anomaly Detection**: Use the Isolation Forest algorithm to detect anomalies in sales data.
- **Model Training**: Train the model using Azure OpenAI.
- **Model Evaluation**: Evaluate the model's performance using various metrics.
- **Hyperparameter Tuning**: Optimize model parameters for better performance.
- **Real-Time Predictions**: Deploy the model to detect real-time sales anomalies using Azure Machine Learning.

## Getting Started

### Prerequisites
- Azure account
- Kaggle account
- Microsoft Fabric
- Python 3.x

### Set Environment Variables
Run the following commands to set your environment variables:
```bash
export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE"
export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE"
```

To check if the variables are correctly set, run:
```bash
echo $AZURE_OPENAI_API_KEY
echo $AZURE_OPENAI_ENDPOINT
```

### Clone Git repo: 
```bash
git clone https://github.com/sophiakobzar/SmartSalesGuard.git
cd SmartSalesGuard
```
### Install required Python packages:
```bash
pip install pandas re openai flask
```

### Run the code:
```bash
python SDKtest.py
```
