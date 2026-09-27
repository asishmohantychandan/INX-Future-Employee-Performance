
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from schemas import EmployeeInput


# --------------------------------------------------
# 1. Application setup
# --------------------------------------------------

app = FastAPI(
    title="INX Employee Performance Prediction API",
    description="Predict employee performance ratings using a trained XGBoost pipeline.",
    version="1.0.0",
)


# --------------------------------------------------
# 2. Load the trained model
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "final_xgboost_employee_performance_model.joblib"
)

model = None

# XGBoost was trained using these internal labels.
LABEL_MAPPING = {
    0: 2,
    1: 3,
    2: 4,
}


@app.on_event("startup")
def load_model():
    global model

    if not MODEL_PATH.exists():
        raise RuntimeError(
            f"Model file not found: {MODEL_PATH}"
        )

    model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# 3. Health endpoint
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
    }


# --------------------------------------------------
# 4. Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict_performance(employee: EmployeeInput):
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not loaded.",
        )

    try:
        # Convert validated input into a DataFrame.
        input_data = pd.DataFrame(
            [employee.model_dump()]
        )

        # Get prediction from the saved pipeline.
        raw_prediction = int(model.predict(input_data)[0])

        # Convert internal XGBoost label to original rating.
        predicted_rating = LABEL_MAPPING[raw_prediction]

        # Get probability for each internal class.
        raw_probabilities = model.predict_proba(input_data)[0]

        probabilities = {
            str(LABEL_MAPPING[int(class_label)]):
                round(float(probability), 6)
            for class_label, probability
            in zip(model.classes_, raw_probabilities)
        }

        return {
            "predicted_performance_rating": predicted_rating,
            "probabilities": probabilities,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(exc)}",
        )