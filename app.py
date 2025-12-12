from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(os.path.join(ROOT, "src"))

from src.synthetic_digital_biomarker.models.light_predict import LightPredictionPipeline

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

model = LightPredictionPipeline()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = {
            "steps_per_day": float(request.form["steps"]),
            "mobility_score": float(request.form["mobility"]),
            "typing_speed": float(request.form["typing_speed"]),
            "reaction_time": float(request.form["reaction_time"])
        }

        result = model.predict(data)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(port=8080, debug=True)
