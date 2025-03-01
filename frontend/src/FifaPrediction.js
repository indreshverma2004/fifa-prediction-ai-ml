import React, { useState, useEffect } from "react";
import axios from "axios";

const FifaPrediction = () => {
  const [teams, setTeams] = useState([]);
  const [selectedTeam, setSelectedTeam] = useState("");
  const [goalsFor, setGoalsFor] = useState("");
  const [goalsAgainst, setGoalsAgainst] = useState("");
  const [win, setWin] = useState("");
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    // Load team names from backend or JSON
    setTeams(["Argentina", "Brazil", "Germany", "France", "Uruguay", "Spain"]); 
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", {
        Team: selectedTeam,
        "Goals For": parseInt(goalsFor),
        "Goals Against": parseInt(goalsAgainst),
        Win: parseInt(win),
      });

      setPrediction(response.data.prediction);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>FIFA World Cup Prediction</h1>
      <form onSubmit={handleSubmit}>
        <label>Team:</label>
        <select value={selectedTeam} onChange={(e) => setSelectedTeam(e.target.value)} required>
          <option value="">Select Team</option>
          {teams.map((team) => (
            <option key={team} value={team}>{team}</option>
          ))}
        </select>
        
        <label>Goals For:</label>
        <input type="number" value={goalsFor} onChange={(e) => setGoalsFor(e.target.value)} required />

        <label>Goals Against:</label>
        <input type="number" value={goalsAgainst} onChange={(e) => setGoalsAgainst(e.target.value)} required />

        <label>Wins:</label>
        <input type="number" value={win} onChange={(e) => setWin(e.target.value)} required />

        <button type="submit">Predict</button>
      </form>

      {prediction && <h2>Prediction: {prediction}</h2>}
    </div>
  );
};

export default FifaPrediction;
