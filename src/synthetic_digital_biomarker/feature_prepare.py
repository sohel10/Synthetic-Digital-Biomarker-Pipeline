import numpy as np
import pandas as pd

# These reflect the distribution of your training data
DEFAULT_MEANS = {
    "wear_time_hours": 12,
    "sleep_quality": 0.75,
    "memory_score": 70,
    "attention_score": 65,
    "executive_function": 60,
}

def prepare_features(user_input: dict):
    """
    Auto-generate all missing biomarker features so your PyTorch/XGB model 
    receives the FULL feature vector it expects.
    
    user_input example:
    {
        "steps_per_day": 5000,
        "mobility_score": 43,
        "typing_speed": 30,
        "reaction_time": 400
    }
    """

    # Convert 4 UI fields into a DataFrame
    df = pd.DataFrame([user_input])

    # ---------------------
    # Auto-fill missing core features
    # ---------------------
    df["wear_time_hours"] = DEFAULT_MEANS["wear_time_hours"]
    df["sleep_quality"] = DEFAULT_MEANS["sleep_quality"]
    df["memory_score"] = DEFAULT_MEANS["memory_score"]
    df["attention_score"] = DEFAULT_MEANS["attention_score"]
    df["executive_function"] = DEFAULT_MEANS["executive_function"]

    # ---------------------
    # Auto-generate engineered features
    # ---------------------

    # variability biomarkers
    df["motor_variability"] = np.abs(df["typing_speed"] - 30)
    df["sleep_variability"] = np.abs(df["sleep_quality"] - 0.75)

    # interaction biomarkers
    df["step_cognition_interaction"] = df["steps_per_day"] * df["memory_score"]
    df["typing_attention_interaction"] = df["typing_speed"] * df["attention_score"]
    df["motor_sleep_interaction"] = df["mobility_score"] * df["sleep_quality"]

    # noise models (simulating wearable uncertainty)
    df["steps_noisy"] = df["steps_per_day"] + np.random.normal(0, 500)
    df["reaction_time_noisy"] = df["reaction_time"] + np.random.normal(0, 30)
    df["sleep_quality_noisy"] = df["sleep_quality"] + np.random.normal(0, 0.03)

    # rolling stats approximations (your model expects these)
    df["steps_mean"] = df["steps_per_day"]
    df["steps_std"] = 0.1 * df["steps_per_day"]
    df["typing_speed_mean"] = df["typing_speed"]
    df["typing_speed_std"] = 0.1 * df["typing_speed"]
    df["rt_slope"] = -0.2 * df["reaction_time"]  # placeholder slope

    return df
