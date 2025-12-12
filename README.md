# Synthetic-Digital-Biomarker-Pipeline# 🧠 Synthetic Digital Biomarker Pipeline  
### End-to-end ML pipeline for generating, cleaning, engineering, and modeling synthetic wearable + cognitive data
📘 Synthetic Digital Biomarker Pipeline

A complete end-to-end ML pipeline for generating, processing, and modeling digital health biomarkers inspired by Apple Watch mobility & cognition research.

## 🚀 Overview

# This project simulates a real-world wearable sensor pipeline, including:

✔ Synthetic data generation (mobility + cognition biomarkers)
✔ Data preprocessing & cleaning
✔ Feature engineering (variability, interactions, noise models)
✔ SQL-style data quality checks
✔ Feature Store creation (production-style tables)
✔ Machine Learning Models

Logistic Regression

XGBoost

# PyTorch MLP (GPU-accelerated)

✔ Modular pipeline architecture
✔ YAML-driven configuration
✔ Ready for deployment or interview demonstration
📂 Project Structure
Synthetic-Digital-Biomarker-Pipeline/
│
├── config/
│   └── params.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
│
├── models/
│   ├── logistic_model.pkl
│   ├── xgb_model.pkl
│   └── torch_model.pt
│
├── notebooks/
│   └── EDA.ipynb
│
├── feature_store/
│   ├── mobility_features.csv
│   └── cognition_features.csv
│
├── src/
│   └── synthetic_digital_biomarker/
│        ├── generate_synthetic_data.py
│        ├── preprocess.py
│        ├── feature_engineering.py
│        ├── feature_store.py
│        ├── sql_pipeline.py
│        ├── sql_qc.py
│        ├── models/
│        │    ├── train_model.py
│        │    ├── torch_model.py
│        │    └── evaluate.py
│        └── __init__.py
│
├── main.py
├── README.md
├── requirements.txt
└── setup.py

ML Model Performance
Model	Accuracy
Logistic Regression	~0.75
XGBoost	~0.75
PyTorch MLP	~0.75

Includes GPU support via CUDA.

Running the Pipeline
python main.py

pandas
numpy
scikit-learn
xgboost
torch
pyyaml




Run this to export as env variables:

1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 404925354687.dkr.ecr.us-east-1.amazonaws.com/kidney
404925354687.dkr.ecr.us-east-1.amazonaws.com/sensor

4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
About MLflow & DVC
MLflow



























