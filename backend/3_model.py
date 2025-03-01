import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

# Load cleaned data
data_file = "../data/cleaned_fifa.csv"  # Adjust path
df = pd.read_csv(data_file)

# Encode team names
encoder = LabelEncoder()
df['team_encoded'] = encoder.fit_transform(df['Team'])

# Features & Labels (Using Goals and Wins to predict Match Outcome)
X = df[['Goals For', 'Goals Against', 'Win']]
y = df['Loss']  # Predicting if the team lost (1) or not (0)

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model & encoders
pickle.dump(model, open("fifa_model.pkl", "wb"))
pickle.dump(encoder, open("encoder.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("✅ Model trained and saved successfully!")
