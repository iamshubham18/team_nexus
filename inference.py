import joblib
import numpy as np


# -----------------------------------
# Load trained TerraSense model
# -----------------------------------

MODEL_PATH = "flood_random_forest.pkl"

model = joblib.load(MODEL_PATH)


# -----------------------------------
# Flood prediction function
# -----------------------------------

def predict_flood(
    water_level,
    rise_rate,
    rainfall,
    soil_moisture
):
    """
    Predict flood risk from sensor values.

    Parameters:
        water_level   : water level in cm
        rise_rate     : rate of water-level increase
        rainfall      : rainfall intensity
        soil_moisture : soil moisture percentage

    Returns:
        Dictionary containing risk and confidence.
    """

    # Arrange values exactly as used during training
    features = np.array([[
        water_level,
        rise_rate,
        rainfall,
        soil_moisture
    ]])

    # ML prediction
    risk = model.predict(features)[0]

    # Probability for each class
    probabilities = model.predict_proba(features)[0]

    # Highest probability
    probability = float(max(probabilities))

    # For this prototype, use the maximum class probability
    # as the model confidence.
    confidence = probability

    return {
        "hazard": "FLOOD",
        "risk": risk,
        "probability": round(probability, 3),
        "confidence": round(confidence, 3)
    }


# -----------------------------------
# Test the model
# -----------------------------------

if __name__ == "__main__":

    result = predict_flood(
    water_level=75,
    rise_rate=3.0,
    rainfall=35,
    soil_moisture=82
)

    print("\n==============================")
    print("       TERRASENSE AI")
    print("==============================")

    print(f"Hazard      : {result['hazard']}")
    print(f"Risk        : {result['risk']}")
    print(f"Probability : {result['probability']:.1%}")
    print(f"Confidence  : {result['confidence']:.1%}")

    print("==============================\n")