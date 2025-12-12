import numpy as np
import pandas as pd
import joblib
import yaml
import torch
from sklearn.preprocessing import StandardScaler
from src.synthetic_digital_biomarker.models.torch_model import MLP

class BiomarkerPredictionPipeline:
    def __init__(self):

        with open("config/params.yaml", "r") as f:
            params = yaml.safe_load(f)

        self.feature_path = params["data_paths"]["features"]
        self.feature_list = pd.read_csv(self.feature_path).drop(columns=["mci_status"]).columns.tolist()

        # load ML models
        self.log_model = joblib.load(params["model"]["model_path"])
        self.xgb_model = joblib.load(params["model"]["xgb_model_path"])

        # load torch model
        input_dim = len(self.feature_list)
        self.torch_model = MLP(input_dim)
        self.torch_model.load_state_dict(
            torch.load(params["model"]["torch_model_path"], map_location="cpu")
        )
        self.torch_model.eval()

        self.scaler = StandardScaler()

    def predict(self, features_dict):
        """features_dict example:
        {
            "steps_per_day": 5000,
            "mobility_score": 55,
            "typing_speed": 40,
            "reaction_time": 320
        }
        """

        df = pd.DataFrame([features_dict])[self.feature_list]
        X = self.scaler.fit_transform(df.values)

        # Predict with each model
        log_p = float(self.log_model.predict_proba(X)[0][1])
        xgb_p = float(self.xgb_model.predict_proba(X)[0][1])

        tensor = torch.tensor(X, dtype=torch.float32)
        torch_p = float(torch.softmax(self.torch_model(tensor), dim=1)[0][1].item())

        ensemble = float(np.mean([log_p, xgb_p, torch_p]))

        return {
            "logistic_regression": log_p,
            "xgboost": xgb_p,
            "pytorch_mlp": torch_p,
            "ensemble_avg": ensemble,
        }
