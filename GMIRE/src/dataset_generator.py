import pandas as pd
import numpy as np

print("Generating Infrastructure Dataset...")

# number of samples
n = 500

# Pipeline dataset
pipe_data = pd.DataFrame({
    "pipe_age": np.random.randint(1, 50, n),
    "pressure": np.random.randint(3, 12, n),
    "soil_corrosion": np.random.randint(1, 10, n),
    "temperature": np.random.randint(20, 45, n),
    "past_leaks": np.random.randint(0, 6, n)
})

# failure risk formula
pipe_data["failure_risk"] = (
    pipe_data["pipe_age"] * 0.3 +
    pipe_data["pressure"] * 0.2 +
    pipe_data["soil_corrosion"] * 0.2 +
    pipe_data["temperature"] * 0.1 +
    pipe_data["past_leaks"] * 0.2
)

# Road dataset
road_data = pd.DataFrame({
    "traffic_load": np.random.randint(1, 10, n),
    "rainfall": np.random.randint(0, 300, n),
    "road_age": np.random.randint(1, 30, n),
    "soil_moisture": np.random.randint(1, 10, n)
})

road_data["damage_risk"] = (
    road_data["traffic_load"] * 0.3 +
    road_data["rainfall"] * 0.3 +
    road_data["road_age"] * 0.2 +
    road_data["soil_moisture"] * 0.2
)

# Save datasets
pipe_data.to_csv("../data/pipe_data.csv", index=False)
road_data.to_csv("../data/road_data.csv", index=False)

print("Datasets generated successfully!")