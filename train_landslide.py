import numpy as np
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# ==========================================
# 1. CREATE SYNTHETIC DATA
# ==========================================

np.random.seed(42)

N = 5000

rainfall = np.random.uniform(0, 100, N)

soil_moisture = np.random.uniform(20, 100, N)

vibration_count = np.random.poisson(5, N)

vibration_duration = np.random.uniform(0, 10, N)

tilt_change = np.random.uniform(0, 10, N)


# ==========================================
# 2. SYNTHETIC LANDSLIDE SEVERITY SCORE
# ==========================================

score = (
    0.25 * (rainfall / 100)
    + 0.25 * (soil_moisture / 100)
    + 0.20 * (vibration_count / 30)
    + 0.15 * (vibration_duration / 10)
    + 0.15 * (tilt_change / 10)
)


# ==========================================
# 3. CREATE RISK LABEL
# ==========================================

risk = np.select(
    [
        score < 0.25,
        score < 0.45,
        score < 0.65
    ],
    [
        "LOW",
        "MEDIUM",
        "HIGH"
    ],
    default="CRITICAL"
)


# ==========================================
# 4. CREATE DATAFRAME
# ==========================================

df = pd.DataFrame({

    "rainfall": rainfall,

    "soil_moisture": soil_moisture,

    "vibration_count": vibration_count,

    "vibration_duration": vibration_duration,

    "tilt_change": tilt_change,

    "risk": risk
})


# ==========================================
# 5. FEATURES
# ==========================================

features = [
    "rainfall",
    "soil_moisture",
    "vibration_count",
    "vibration_duration",
    "tilt_change"
]

X = df[features]

y = df["risk"]


# ==========================================
# 6. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================
# 7. RANDOM FOREST
# ==========================================

model = RandomForestClassifier(

    n_estimators=120,

    max_depth=8,

    random_state=42,

    class_weight="balanced",

    n_jobs=-1
)


model.fit(X_train, y_train)


# ==========================================
# 8. EVALUATION
# ==========================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n===================================")
print("     TERRASENSE LANDSLIDE AI")
print("===================================")

print(
    f"\nAccuracy: {accuracy:.2%}"
)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions
    )
)


# ==========================================
# 9. SAVE DATASET
# ==========================================

df.to_csv(
    "landslide_synthetic_dataset.csv",
    index=False
)


# ==========================================
# 10. SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "landslide_random_forest.pkl"
)


print("\n===================================")

print(
    "Dataset saved:"
)

print(
    "landslide_synthetic_dataset.csv"
)

print(
    "\nModel saved:"
)

print(
    "landslide_random_forest.pkl"
)

print("===================================")