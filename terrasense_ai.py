# ============================================
#        TERRASENSE AI - HAZARD ENGINE
# ============================================
# Current hardware inputs:
#   1. Flame detection
#   2. Vibration detection
#   3. Flood detection
#
# This program converts hardware status
# into hazard risk and alerts.
# ============================================


def assess_hazards(flame_detected, vibration_detected, flood_detected):

    alerts = []

    # ----------------------------------------
    # FIRE / FLAME
    # ----------------------------------------

    if flame_detected:
        fire_risk = "CRITICAL"
        fire_priority = "CRITICAL"
        fire_message = "Fire/flame detected."
        fire_action = "Immediate fire emergency response recommended."

    else:
        fire_risk = "LOW"
        fire_priority = "INFO"
        fire_message = "No fire detected."
        fire_action = "Continue monitoring."


    # ----------------------------------------
    # FLOOD
    # ----------------------------------------

    if flood_detected:
        flood_risk = "CRITICAL"
        flood_priority = "CRITICAL"
        flood_message = "Flood conditions detected."
        flood_action = "Activate flood response measures."

    else:
        flood_risk = "LOW"
        flood_priority = "INFO"
        flood_message = "Flood conditions are currently normal."
        flood_action = "Continue monitoring."


    # ----------------------------------------
    # LANDSLIDE
    # ----------------------------------------
    #
    # Using the available vibration sensor.
    #
    # Vibration alone = WARNING
    # Flood + vibration = CRITICAL
    #
    # This is a prototype rule-based layer
    # using currently available hardware.
    # ----------------------------------------

    if vibration_detected and flood_detected:

        landslide_risk = "CRITICAL"
        landslide_priority = "CRITICAL"
        landslide_message = "Flood conditions with abnormal vibration detected. High landslide danger."
        landslide_action = "Immediate landslide risk response recommended."

    elif vibration_detected:

        landslide_risk = "HIGH"
        landslide_priority = "HIGH"
        landslide_message = "Abnormal ground vibration detected. Possible landslide activity."
        landslide_action = "Inspect the area and monitor vibration continuously."

    else:

        landslide_risk = "LOW"
        landslide_priority = "INFO"
        landslide_message = "No abnormal ground vibration detected."
        landslide_action = "Continue monitoring."


    # ----------------------------------------
    # CREATE ALERT LIST
    # ----------------------------------------

    alerts.append({
        "hazard": "FIRE",
        "risk": fire_risk,
        "priority": fire_priority,
        "message": fire_message,
        "action": fire_action
    })

    alerts.append({
        "hazard": "FLOOD",
        "risk": flood_risk,
        "priority": flood_priority,
        "message": flood_message,
        "action": flood_action
    })

    alerts.append({
        "hazard": "LANDSLIDE",
        "risk": landslide_risk,
        "priority": landslide_priority,
        "message": landslide_message,
        "action": landslide_action
    })

    return alerts


# ============================================
# DISPLAY FUNCTION
# ============================================

def display_results(alerts):

    print("\n")
    print("============================================")
    print("             TERRASENSE AI")
    print("      ENVIRONMENTAL EARLY WARNING")
    print("============================================")

    for alert in alerts:

        print("\n--------------------------------------------")
        print(f"Hazard   : {alert['hazard']}")
        print(f"Risk     : {alert['risk']}")
        print(f"Priority : {alert['priority']}")
        print(f"Message  : {alert['message']}")
        print(f"Action   : {alert['action']}")

    print("--------------------------------------------")
    print("============================================")


# ============================================
# MAIN TEST
# ============================================

if __name__ == "__main__":

    # ----------------------------------------
    # CHANGE THESE VALUES TO TEST
    # ----------------------------------------

    flame_detected = False
    vibration_detected = True
    flood_detected = False

    # ----------------------------------------
    # RUN TERRASENSE AI
    # ----------------------------------------

    results = assess_hazards(
        flame_detected,
        vibration_detected,
        flood_detected
    )

    display_results(results)