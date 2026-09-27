import joblib
import pandas as pd


# ==========================================
# LOAD MODEL
# ==========================================

MODEL_PATH = "landslide_random_forest.pkl"

model = joblib.load(MODEL_PATH)


# ==========================================
# LANDSLIDE PREDICTION
# ==========================================

def predict_landslide(
    rainfall,
    soil_moisture,
    vibration_count,
    vibration_duration,
    tilt_change
):
    """
    Predict landslide risk.

    Current model is a prototype trained
    using synthetic data.
    """

    # IMPORTANT:
    # Use a DataFrame with the SAME feature
    # names and order used during training.

    features = pd.DataFrame([{
        "rainfall": rainfall,
        "soil_moisture": soil_moisture,
        "vibration_count": vibration_count,
        "vibration_duration": vibration_duration,
        "tilt_change": tilt_change
    }])

    # Prediction
    risk = model.predict(features)[0]

    # Probabilities
    probabilities = model.predict_proba(features)[0]

    confidence = float(max(probabilities))

    return {
        "hazard": "LANDSLIDE",
        "risk": risk,
        "probability": round(confidence, 3),
        "confidence": round(confidence, 3)
    }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    result = predict_landslide(
        rainfall=45,
        soil_moisture=82,
        vibration_count=18,
        vibration_duration=4.2,
        tilt_change=3.5
    )

    print("\n================================")
    print("       TERRASENSE AI")
    print("================================")

    print(f"Hazard      : {result['hazard']}")
    print(f"Risk        : {result['risk']}")
    print(f"Probability : {result['probability']:.1%}")
    print(f"Confidence  : {result['confidence']:.1%}")

    print("================================\n")