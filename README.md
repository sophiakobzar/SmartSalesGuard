# SmartSalesGuard

## Project Overview
SalesAnomalyDetection is a project aimed at detecting anomalies in sales data to identify unusual patterns or potential fraud for an online Super Store. This project leverages Microsoft Fabric and Azure OpenAI services to process and analyze data, providing real-time insights and anomaly detection.

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
- Python 3.x
- Azure CLI
- pgAdmin or Azure Data Factory

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SalesAnomalyDetection.git
   cd SalesAnomalyDetection
