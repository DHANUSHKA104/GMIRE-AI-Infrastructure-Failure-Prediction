import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

print("Training AI Model...")

# load dataset
data = pd.read_csv("../data/pipe_data.csv")

# input features
X = data[["pipe_age","pressure","soil_corrosion","temperature","past_leaks"]]

# target variable
y = data["failure_risk"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = RandomForestRegressor()

# train model
model.fit(X_train, y_train)

# save model
joblib.dump(model, "../data/pipeline_model.pkl")

print("Model trained and saved successfully!")