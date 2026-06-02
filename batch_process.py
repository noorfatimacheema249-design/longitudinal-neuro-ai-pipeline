import os
import SimpleITK as sitk
import numpy as np
import pandas as pd

# Direct paths to your master directory
base_dir = r"C:\Users\noorf\Downloads\ASNR-MICCAI-BraTS2023-GLI-Challenge-ValidationData\ASNR-MICCAI-BraTS2023-GLI-Challenge-ValidationData"
output_csv = r"C:\Users\noorf\OneDrive\Documents\AHA 2026\brain_features_output.csv"

print("🚀 Starting automated clinical batch extraction...")

# Gather all patient folders inside the directory
patient_folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]


target_folders = patient_folders

all_patient_data = []

for folder_name in target_folders:
    print(f"🔄 Processing patient scan: {folder_name}...")
    
    # Construct the file path dynamically to the t1c scan for each patient
    scan_file_name = f"{folder_name}-t1c.nii.gz"
    full_scan_path = os.path.join(base_dir, folder_name, scan_file_name)
    
    # Verify the file actually exists before loading it
    if not os.path.exists(full_scan_path):
        print(f"⚠️ Warning: Missing scan file for {folder_name}. Skipping.")
        continue
        
    try:
        # Load image via SimpleITK engine
        image = sitk.ReadImage(full_scan_path)
        array = sitk.GetArrayFromImage(image)
        
        # Filter brain tissue from surrounding background
        brain_tissue = array[array > 100]
        
        # Calculate raw texture biomarkers
        mean_val = np.mean(brain_tissue)
        std_val = np.std(brain_tissue)
        heterogeneity = (std_val / mean_val) * 100
        max_intensity = int(np.max(array))
        
        # Save individual patient metrics into a dictionary
        patient_metrics = {
            "Patient_ID": folder_name,
            "Mean_Signal_Intensity": round(mean_val, 2),
            "Microvascular_Deviation": round(std_val, 2),
            "Heterogeneity_Index_Percent": round(heterogeneity, 2),
            "Peak_Contrast_Intensity": max_intensity
        }
        
        all_patient_data.append(patient_metrics)
        
    except Exception as e:
        print(f"❌ Failed to process folder {folder_name}: {e}")

# Step 2: Convert accumulated data array into a clean spreadsheet
df = pd.DataFrame(all_patient_data)
df.to_csv(output_csv, index=False)

print(f"\n📊 SUCCESS! Batch feature extraction complete.")
print(f"💾 Clean data array exported directly to: {output_csv}")
print(df.head())
