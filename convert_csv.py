import pandas as pd

# Load CSV
df = pd.read_csv("placement.csv")

# Convert all columns except target to float
for col in df.columns:
    if col != 'placed':
        df[col] = df[col].astype(float)

# Save updated CSV
df.to_csv("placement.csv", index=False)

print("✅ CSV converted to float successfully!")