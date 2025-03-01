import pandas as pd
import os

# Define the correct file path (since cleaned_fifa.csv is in the 'data' folder)
data_file = os.path.join("..", "data", "cleaned_fifa.csv")

# Check if the file exists
if not os.path.exists(data_file):
    raise FileNotFoundError(f"⚠️ Data file not found: {data_file}\nCheck the 'data' folder.")

# Load CSV
df = pd.read_csv(data_file)

# Print basic information
print("✅ CSV loaded successfully!")
print("Columns in dataset:", df.columns)
print(df.head())  # Show first few rows
