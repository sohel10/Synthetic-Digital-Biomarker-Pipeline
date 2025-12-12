import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "synthetic_digital_biomarker"

list_of_files = [
    # GitHub workflow placeholder
    ".github/workflows/.gitkeep",

    # Config directory
    "config/params.yaml",

    # Data directories
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/features/.gitkeep",

    # Source code files
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/generate_synthetic_data.py",
    f"src/{project_name}/preprocess.py",
    f"src/{project_name}/feature_engineering.py",

    # Model training + evaluation
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/train_model.py",
    f"src/{project_name}/models/evaluate.py",

    # Notebooks
    "notebooks/EDA.ipynb",

    # Templates (optional)
    "templates/index.html",

    # Project roots
    "README.md",
    "requirements.txt",
    "setup.py",
    "main.py",
    "app.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if not exists
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    # Create empty file if it doesn't exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
