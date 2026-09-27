def generate_alert(prediction):

    hazard = prediction["hazard"]
    risk = prediction["risk"]

    # Convert hazard name for messages
    hazard_name = hazard.lower()

    if risk == "LOW":

        priority = "INFO"
        message = f"{hazard_name.capitalize()} conditions are currently normal."
        action = "Continue monitoring."

    elif risk == "MEDIUM":

        priority = "WARNING"
        message = f"{hazard_name.capitalize()} risk is increasing."
        action = "Monitor sensor conditions closely."

    elif risk == "HIGH":

        priority = "HIGH"
        message = f"High probability of {hazard_name} detected."
        action = f"Prepare {hazard_name} response measures."

    elif risk == "CRITICAL":

        priority = "CRITICAL"
        message = f"Critical {hazard_name} conditions detected."
        action = "Immediate emergency response recommended."

    else:

        priority = "INFO"
        message = "Unknown risk state."
        action = "Check sensor and model status."

    return {
        "priority": priority,
        "message": message,
        "action": action
    }