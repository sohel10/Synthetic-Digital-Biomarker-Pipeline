import pandas as pd
import yaml
import os

def load_params():
    with open("config/params.yaml", "r") as f:
        return yaml.safe_load(f)

def feature_engineering():
    params = load_params()
    df = pd.read_csv(params["data_paths"]["processed"])

    window = params["features"]["rolling_window"]

    # Rolling features
    df["steps_mean"] = df["steps_per_day"].rolling(window).mean()
    df["steps_std"] = df["steps_per_day"].rolling(window).std()

    df["typing_speed_mean"] = df["typing_speed"].rolling(window).mean()
    df["typing_speed_std"] = df["typing_speed"].rolling(window).std()

    df["rt_slope"] = df["reaction_time"].diff()

    # Drop initial rows with NA from rolling
    df = df.dropna()

    os.makedirs("data/features", exist_ok=True)
    df.to_csv(params["data_paths"]["features"], index=False)
    print("Feature engineering complete → data/features/feature_data.csv")

if __name__ == "__main__":
    feature_engineering()
