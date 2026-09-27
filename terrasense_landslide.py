from landslide_inference import predict_landslide
from alert_engine import generate_alert


def run_landslide():

    # -----------------------------
    # TEST SENSOR VALUES
    # -----------------------------

    rainfall = 45
    soil_moisture = 82
    vibration_count = 18
    vibration_duration = 4.2
    tilt_change = 3.5

    # -----------------------------
    # AI PREDICTION
    # -----------------------------

    prediction = predict_landslide(
        rainfall=rainfall,
        soil_moisture=soil_moisture,
        vibration_count=vibration_count,
        vibration_duration=vibration_duration,
        tilt_change=tilt_change
    )

    # -----------------------------
    # ALERT GENERATION
    # -----------------------------

    alert = generate_alert(prediction)

    # -----------------------------
    # DISPLAY
    # -----------------------------

    print("================================")
    print("       TERRASENSE AI")
    print("================================")

    print("Hazard      : LANDSLIDE")
    print(f"Risk        : {prediction['risk']}")
    print(f"Probability : {prediction['probability'] * 100:.1f}%")
    print(f"Confidence  : {prediction['confidence'] * 100:.1f}%")

    print("--------------------------------")

    print(f"Priority    : {alert['priority']}")
    print(f"Message     : {alert['message']}")
    print(f"Action      : {alert['action']}")

    print("================================")


if __name__ == "__main__":
    run_landslide()