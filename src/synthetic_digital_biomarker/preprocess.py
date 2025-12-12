import pandas as pd
import yaml
import os

def load_params():
    with open("config/params.yaml", "r") as f:
        return yaml.safe_load(f)

def preprocess_data():
    params = load_params()
    df = pd.read_csv(params["data_paths"]["raw"])

    # QC filters
    df = df[df["wear_time_hours"] >= params["preprocess"]["min_wear_time"]]
    df = df[(df["reaction_time"] >= params["preprocess"]["rt_min"]) &
            (df["reaction_time"] <= params["preprocess"]["rt_max"])]

    # Remove missing values
    df = df.dropna()

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(params["data_paths"]["processed"], index=False)
    print("Preprocessing complete → data/processed/clean_data.csv")

if __name__ == "__main__":
    preprocess_data()
