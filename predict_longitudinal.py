import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

paired_csv_path = r"C:\Users\noorf\OneDrive\Documents\AHA 2026\longitudinal_paired_output.csv"

# Load the longitudinal matrix you just built
df = pd.read_csv(paired_csv_path)

# Define X (Predictor: Baseline Contrast Intensity) and Y (Target: Future Change in Chaos)
X = df[['Peak_Contrast_Intensity_Baseline']].values
y = df['Chaos_Delta_Percent'].values

print("🤖 Initializing Predictive Linear Machine Learning Model...")

# Train the regression algorithm
model = LinearRegression()
model.fit(X, y)

# Extract mathematical coefficients
slope = model.coef_[0]
intercept = model.intercept_
r_squared = model.score(X, y)

print("\n📊 MACHINE LEARNING FORECASTING OUTPUT:")
print(f"🔹 Model Slope (Weight Coefficient): {slope:.6f}")
print(f"🔹 Model Baseline Intercept:         {intercept:.2f}")
print(f"🔹 Calculated Model R² Score:         {r_squared:.4f}")

print("\n🔮 PREDICTIVE PARADIGM FUNCTION:")
print(f"Future Tissue Chaos Change % = ({slope:.6f} * Baseline_Contrast) + ({intercept:.2f})")

# Test a prediction on a brand new hypothetical patient scan
test_baseline_signal = 12000
predicted_delta = (slope * test_baseline_signal) + intercept
print(f"\n🧠 Clinical Prediction Test: If a new patient shows an initial baseline signal of {test_baseline_signal},")
print(f"   the model forecasts their structural tissue chaos will change by {predicted_delta:.2f}% by follow-up.")
