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
- Git Bash

### Clone Git repo: 
```bash
git clone https://github.com/sophiakobzar/SmartSalesGuard.git
cd SmartSalesGuard
```
### Install required Python packages:
```bash
pip install pandas re openai flask
```


## Deploy the website

### Run the Website:
```bash
python server.py
```
then go to http://127.0.0.1:5000 to view website

