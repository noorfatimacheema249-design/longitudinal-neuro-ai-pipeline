import pandas as pd
import numpy as np

# Create a minimal, elegant plot manual matrix since matplotlib isn't installed
paired_csv_path = r"C:\Users\noorf\OneDrive\Documents\AHA 2026\longitudinal_paired_output.csv"
df = pd.read_csv(paired_csv_path)

print("📈 Generating Text-Based Data Distribution Map...\n")
print(f"{'Patient ID':<18} | {'Baseline Contrast (X)':<22} | {'Chaos Delta % (Y)':<18}")
print("-" * 65)

for idx, row in df.sort_values(by='Peak_Contrast_Intensity_Baseline').iterrows():
    print(f"{row['Base_ID']:<18} | {row['Peak_Contrast_Intensity_Baseline']:<22.0f} | {row['Chaos_Delta_Percent']:<18.2f}%")

print("\n✅ Matrix mapped cleanly! Ready to copy results directly into your clinical abstract write-up.")
