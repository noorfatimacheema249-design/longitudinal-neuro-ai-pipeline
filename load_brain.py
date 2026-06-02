import SimpleITK as sitk
import numpy as np

scan_path = r"C:\Users\noorf\Downloads\ASNR-MICCAI-BraTS2023-GLI-Challenge-ValidationData\ASNR-MICCAI-BraTS2023-GLI-Challenge-ValidationData\BraTS-GLI-00467-000\BraTS-GLI-00467-000-t1c.nii.gz"

print("🔬 Extracting digital pathology metrics from brain voxels...")

try:
    brain_image = sitk.ReadImage(scan_path)
    brain_array = sitk.GetArrayFromImage(brain_image)
    
    # 1. Filter out the black background (air around the skull) to only analyze brain tissue
    # We ignore pixels close to 0
    brain_tissue = brain_array[brain_array > 100]
    
    # 2. Calculate fundamental statistical metrics of tissue texture
    mean_intensity = np.mean(brain_tissue)
    std_intensity = np.std(brain_tissue)
    
    # Coefficient of Variation: Measures relative structural chaos/heterogeneity
    tissue_heterogeneity = (std_intensity / mean_intensity) * 100
    
    print("\n📊 EXTRACTED BIOMARKERS FOR PATIENT 00467:")
    print(f"🔹 Mean Parenchymal Signal Intensity:   {mean_intensity:.2f}")
    print(f"🔹 Tissue Micro-Structural Deviation:   {std_intensity:.2f}")
    print(f"🔹 Calculated Tissue Heterogeneity Index: {tissue_heterogeneity:.2f}%")
    
    # Clinical sanity check
    if tissue_heterogeneity > 50:
        print("⚠️ Interpretation: High tissue texture chaos detected. Suggests complex vascular structural decay.")
    else:
        print("✅ Interpretation: Homogenous tissue texture detected.")

except Exception as e:
    print(f"\n❌ Error processing image matrices: {e}")
