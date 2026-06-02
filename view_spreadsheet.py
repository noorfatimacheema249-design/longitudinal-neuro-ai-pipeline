import pandas as pd

csv_path = r"C:\Users\noorf\OneDrive\Documents\AHA 2026\brain_features_output.csv"

# Load the file you just created
df = pd.read_csv(csv_path)

print("📝 YOUR EXTRACTED BRAIN BIOMARKER SPREADSHEET:")
print(df.to_string())
