import joblib
import numpy as np

print("\nGMIRE - Pipeline Failure Prediction System\n")

# load trained model
model = joblib.load("../data/pipeline_model.pkl")

# user inputs
pipe_age = int(input("Enter Pipe Age: "))
pressure = int(input("Enter Pressure: "))
soil_corrosion = int(input("Enter Soil Corrosion Level: "))
temperature = int(input("Enter Temperature: "))
past_leaks = int(input("Enter Number of Past Leaks: "))

# prepare input
data = np.array([[pipe_age, pressure, soil_corrosion, temperature, past_leaks]])

# prediction
prediction = model.predict(data)

risk_score = prediction[0]

print("\nPredicted Failure Risk Score:", round(risk_score,2))

# risk classification
if risk_score < 8:
    risk = "LOW"
    action = "Routine Monitoring Recommended"

elif risk_score < 15:
    risk = "MEDIUM"
    action = "Schedule Maintenance Inspection"

else:
    risk = "HIGH"
    action = "Immediate Inspection Required"

print("\nRisk Level:", risk)
print("Recommended Action:", action)