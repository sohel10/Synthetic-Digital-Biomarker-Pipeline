## 🧠 Synthetic-Digital-Biomarker-Pipeline
## 🧬 End-to-End Synthetic Digital Biomarker Pipeline (Wearables + Cognition + ML)

This project simulates an end-to-end digital biomarker pipeline similar to Apple Watch mobility & cognition research.

It generates synthetic wearable data, cleans it, engineers features, performs QC, builds a feature store, and trains ML models:

Mobility biomarkers Cognition biomarkers Deep-learning inspired synthetic pattern generation

Multi-model analytics (Logistic Regression, XGBoost, PyTorch MLP)

A modular, production-style ML system designed for portfolio, interviews, and real-world pipelines.

<p align="center"> <img src="digital.png" width="90%" alt="Synthetic Digital Biomarker Pipeline Banner"> </p>
# 🔍 2. What This Pipeline Includes
✔ Synthetic Data Generation

Mobility + cognition biomarkers (step stability, gait variability, reaction time, memory tests)

✔ Data Preprocessing

Cleaning Scaling Noise modeling Outlier correction

Variability features
Temporal aggregations
Interaction features

✔ SQL-Style QC

Missingness checks
Range validation
Consistency rules

✔ Feature Store

Production-style tables for ML ingestion

✔ Machine Learning Models

Logistic Regression XGBoost PyTorch MLP (GPU accelerated)

✔ YAML Configuration + Modular Architecture

Clean, extensible, interview-ready design.

# 🧠 3. Model Outputs (Example Visuals)
📊 Random Prediction Example

(Optional — once your model outputs a prediction grid, add it here)

<p align="center"> <img src="prediction_example.png" width="85%" alt="Prediction Grid Example"> </p>
# 🔥 4. Model Architecture: PyTorch MLP (GPU-Accelerated)

The deep learning model includes:

Input normalization Two hidden layers ReLU activation Dropout regularization CUDA acceleration when available

# Used for risk prediction and biomarker classification tasks.

# 📂 5. Project Structure (Clean Markdown Tree)
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
├── src/synthetic_digital_biomarker/
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
├── requirements.txt
└── setup.py

# 📈 6. Model Performance Summary
Metric	Score
Logistic Regression	~0.75
XGBoost	~0.75
PyTorch MLP	~0.75

Includes GPU support via CUDA.

# 🧪 7. Training + Pipeline Workflow (MLOps Overview)

The entire project follows a production-grade ML workflow:

✔ Modular Code Design

src/synthetic_digital_biomarker/ contains reusable functions and pipelines.

✔ Configuration via YAML

Edit parameters in config/params.yaml.

✔ Experiment Tracking

(Mlflow-ready structure)

✔ Data Versioning (Optional DVC Integration)

Raw → processed → feature store

✔ CI/CD Ready

Supports GitHub Actions, Docker, AWS EC2/ECR deployment.

# 🧠 8. Why This Pipeline Matters

Digital biomarkers enable:

Early detection

Longitudinal monitoring

Cognitive health assessment

Mobility decline tracking

Wearable-based risk profiling

Your pipeline demonstrates end-to-end mastery of ML systems, from raw signal → features → models → deployment structure.

# 🚀 9. How to Run the Project
git clone https://github.com/sohel10/Synthetic-Digital-Biomarker-Pipeline
cd Synthetic-Digital-Biomarker-Pipeline

pip install -r requirements.txt
python main.py

# 🧰 10. Technologies Used

Python 3.10

pandas

numpy

scikit-learn

xgboost

torch (GPU accelerated)

pyyaml

# 📦 11. Deployment (Optional AWS CI/CD)

Same structure as your kidney project:

Create IAM user

Build Docker image

Push image to ECR

Deploy to EC2

Configure GitHub Actions → self-hosted runner

Launch model API

# 📜 License

MIT License.
