import os
import pandas as pd

# ✅ Define file paths
file_path = r"C:\Users\indre\.cache\kagglehub\datasets\iamsouravbanerjee\fifa-football-world-cup-dataset\versions\8\fifa.csv"
processed_file_path = r"C:\Users\indre\Desktop\Books\coding\aiml\fifa-prediction\data\cleaned_fifa.csv"

# ✅ Ensure the target directory exists
output_dir = os.path.dirname(processed_file_path)
os.makedirs(output_dir, exist_ok=True)  # ✅ Create directory if it doesn't exist

# ✅ Load dataset
df = pd.read_csv(file_path)

# ✅ Print actual column names
print("Original dataset shape:", df.shape)
print("Columns in dataset:", df.columns)

# ✅ Example column selection (Update based on actual dataset)
columns_to_keep = ["Team", "Games Played", "Win", "Loss", "Goals For", "Goals Against"]
df = df[columns_to_keep]

# ✅ Handle missing values
df.dropna(inplace=True)

# ✅ Save cleaned data
df.to_csv(processed_file_path, index=False)

print("\n✅ Cleaned dataset saved at:", processed_file_path)
print("Cleaned dataset shape:", df.shape)
print(df.head())
