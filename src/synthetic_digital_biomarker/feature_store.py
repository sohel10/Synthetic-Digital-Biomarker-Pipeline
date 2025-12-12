import pandas as pd
import os

def safe_select(df, columns):
    """Select only columns that exist in the dataframe."""
    return df[[col for col in columns if col in df.columns]]


def build_feature_store():

    print("\n🧱 Building Feature Store Tables...")

    features = pd.read_csv("data/features/feature_data.csv")

    # -------------------------------
    # Feature table 1: Mobility
    # -------------------------------
    mobility_cols = [
        "steps_per_day",
        "mobility_score",
        "typing_speed",
        "motor_variability",
        "motor_sleep_interaction"
    ]
    mobility = safe_select(features, mobility_cols)

    # -------------------------------
    # Feature table 2: Cognition
    # -------------------------------
    cognition_cols = [
        "reaction_time",
        "memory_score",
        "attention_score",
        "executive_function",
        "cog_interaction",
        "attention_interaction"
    ]
    cognition = safe_select(features, cognition_cols)

    # Save outputs
    os.makedirs("feature_store", exist_ok=True)
    mobility.to_csv("feature_store/mobility_features.csv", index=False)
    cognition.to_csv("feature_store/cognition_features.csv", index=False)

    print("✅ Feature Store built → feature_store/")
