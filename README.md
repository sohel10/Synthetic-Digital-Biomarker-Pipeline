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
