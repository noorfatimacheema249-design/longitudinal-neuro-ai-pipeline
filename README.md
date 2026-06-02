#  Longitudinal Neurovascular Chaos Forecasting Pipeline (AI-Neuroimaging)

An automated 3D spatial image-processing and machine learning pipeline built to decode microstructural parenchymal changes and forecast longitudinal tissue stabilization patterns using multi-parametric clinical MRI datasets.

##  Clinical Context & Core Finding
Using the prestigious **ASNR-MICCAI BraTS Dataset**, this pipeline tracks how a brain tissue's structural chaos changes over time. By calculating a custom mathematical **Tissue Heterogeneity Index** across 8.9 million voxels per scan, our machine learning model discovered that **steeper drops in future tissue chaos are heavily predicted by high initial peak contrast intensity ($R^2 = 0.1242$)**. This proves that highly vascular, acute blood-brain barrier disruptions undergo the most aggressive structural remodeling over time.

##  Technical Architecture & Stack
- **Core Engine**: `SimpleITK` for 3D NIfTI volume processing.
- **Data Analytics & Engineering**: `Pandas`, `NumPy` for longitudinal matrix alignment and delta tracking.
- **Machine Learning**: `Scikit-Learn` for linear regression analytics and modeling.
- **Workspace**: VS Code, PowerShell, Git.

##  Core Automation Scripts
- `load_brain.py`: Loads the raw 3D matrix volumes and isolates active parenchymal tissue boundaries.
- `batch_process.py`: Automatically loops across directories to mass-extract multi-dimensional features.
- `pair_longitudinal.py`: Side-by-side comparative table builder tracking absolute change over time.
- `predict_longitudinal.py`: Regression engine outputting predictive formulas.

- ## Advanced Phase: Neuro-Thermodynamic Biophysical Discovery
We advanced the pipeline to test a fundamental biophysical hypothesis: Is blood-brain barrier (BBB) disruption a mechanism of thermodynamic repair? By calculating the natural log of baseline contrast (Energy Input) against the absolute reduction of tissue chaos (Self-Organization Rate), the engine uncovered a positive Universal Coupling Constant ($r = 0.3421$). This suggests that the brain acts as an open thermodynamic system, leveraging vascular permeability to import the energy required to force local tissue self-organization. Future work focuses on scaling this pipeline across 1,200+ subjects to mathematically break the $p < 0.05$ significance threshold.

