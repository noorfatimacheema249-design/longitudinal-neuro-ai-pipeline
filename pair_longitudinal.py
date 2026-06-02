import pandas as pd
import numpy as np

csv_path = r"C:\Users\noorf\OneDrive\Documents\AHA 2026\brain_features_output.csv"
output_paired_csv = r"C:\Users\noorf\OneDrive\Documents\AHA 2026\longitudinal_paired_output.csv"

# Load your master spreadsheet
df = pd.read_csv(csv_path)

# 1. Extract the base Patient ID (e.g., BraTS-GLI-00001) and the Scan Timepoint (000 or 001)
df['Base_ID'] = df['Patient_ID'].apply(lambda x: "-".join(x.split("-")[:-1]))
df['Timepoint'] = df['Patient_ID'].apply(lambda x: x.split("-")[-1])

# 2. Separate out the baseline scans and follow-up scans into distinct tables
baseline_df = df[df['Timepoint'] == '000'].copy()
followup_df = df[df['Timepoint'] == '001'].copy()

# 3. Merge them side-by-side using the matching Base_ID
paired_df = pd.merge(baseline_df, followup_df, on='Base_ID', suffixes=('_Baseline', '_FollowUp'))

# 4. Calculate the Longitudinal Delta (Absolute change in tissue chaos over time)
paired_df['Chaos_Delta_Percent'] = paired_df['Heterogeneity_Index_Percent_FollowUp'] - paired_df['Heterogeneity_Index_Percent_Baseline']

# Keep only the cleanest, high-yield columns for analysis
final_columns = [
    'Base_ID', 
    'Heterogeneity_Index_Percent_Baseline', 
    'Heterogeneity_Index_Percent_FollowUp',
    'Chaos_Delta_Percent',
    'Peak_Contrast_Intensity_Baseline'
]
paired_df = paired_df[final_columns]

# Save your new longitudinal table
paired_df.to_csv(output_paired_csv, index=False)

print("📊 LONGITUDINAL PAIRING MATRIX COMPLETE!\n")
print(paired_df.to_string())
