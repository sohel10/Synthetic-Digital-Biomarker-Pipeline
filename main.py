from src.synthetic_digital_biomarker.generate_synthetic_data import generate_synthetic_data
from src.synthetic_digital_biomarker.preprocess import preprocess_data
from src.synthetic_digital_biomarker.feature_engineering import feature_engineering
from src.synthetic_digital_biomarker.models.train_model import train_models
from src.synthetic_digital_biomarker.models.evaluate import evaluate_models
from src.synthetic_digital_biomarker.models.torch_model import train_torch_model
from src.synthetic_digital_biomarker.sql_pipeline import run_sql_pipeline
from src.synthetic_digital_biomarker.sql_pipeline import run_sql_pipeline
from src.synthetic_digital_biomarker.sql_qc import run_sql_qc
from src.synthetic_digital_biomarker.feature_store import build_feature_store

if __name__ == "__main__":
    
    print("\nSTEP 1: Generating Synthetic Data...")
    generate_synthetic_data()

    print("\nSTEP 2: Preprocessing...")
    preprocess_data()

    print("\nSTEP 3: Feature Engineering...")
    feature_engineering()

    print("\nSTEP 4: Training Models...")
    train_models()

    print("\nSTEP 5: Evaluating Models...")
    evaluate_models()

    print("\nSTEP 6: Training PyTorch Deep Learning Model...")
    train_torch_model()

    print("\nSTEP 1B: Running SQL Data Pipeline...")
    run_sql_pipeline()

    print("\nSTEP 1B: SQL Pipeline...")
    run_sql_pipeline()

    print("\nSTEP 1C: SQL Data Quality Checks...")
    run_sql_qc()

    print("\nSTEP 3B: Building Feature Store Tables...")
    build_feature_store()