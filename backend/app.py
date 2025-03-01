import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load trained model & preprocessors
model = pickle.load(open("fifa_model.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow all origins (Fix CORS issue)

@app.route("/")
def home():
    return "🏆 FIFA Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        # Validate input
        required_fields = ["Team", "Goals For", "Goals Against", "Win"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing input fields"}), 400
        
        # Encode team name
        team_encoded = encoder.transform([data["Team"]])[0]
        
        # Prepare input features
        features = np.array([[data["Goals For"], data["Goals Against"], data["Win"]]])
        features_scaled = scaler.transform(features)

        # Predict
        prediction = model.predict(features_scaled)[0]
        result = "Lose" if prediction == 1 else "Not Lose"

        return jsonify({"team": data["Team"], "prediction": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
