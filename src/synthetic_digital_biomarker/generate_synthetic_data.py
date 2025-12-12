import numpy as np
import pandas as pd
import yaml
import os

def load_params():
    with open("config/params.yaml", "r") as f:
        return yaml.safe_load(f)

def generate_synthetic_data():
    params = load_params()
    n = params["synthetic"]["n_samples"]

    np.random.seed(params["synthetic"]["random_seed"])

    data = pd.DataFrame({
        "steps_per_day": np.random.normal(6000, 2000, n),
        "mobility_score": np.random.normal(50, 10, n),
        "typing_speed": np.random.normal(40, 8, n),
        "wear_time_hours": np.random.uniform(5, 16, n),
        "sleep_quality": np.random.normal(0.75, 0.1, n),

        "reaction_time": np.random.normal(450, 80, n),
        "memory_score": np.random.normal(70, 10, n),
        "attention_score": np.random.normal(65, 12, n),
        "executive_function": np.random.normal(60, 15, n),

        # Binary label: MCI = 1
        "mci_status": np.random.binomial(1, 0.25, n)
    })

    os.makedirs("data/raw", exist_ok=True)
    data.to_csv("data/raw/synthetic_data.csv", index=False)
    print("Synthetic data generated → data/raw/synthetic_data.csv")

if __name__ == "__main__":
    generate_synthetic_data()
