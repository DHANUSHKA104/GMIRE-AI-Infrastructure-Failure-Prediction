# GMIRE – AI Infrastructure Failure Prediction

## Overview

GMIRE is an AI-based prototype that predicts pipeline infrastructure failures using machine learning.

The system analyzes infrastructure parameters like pipe age, pressure, temperature, and soil moisture to determine the risk of pipeline failure.

## Project Workflow

1. Dataset Generation
   Infrastructure datasets are generated for pipelines.

2. Model Training
   A machine learning model is trained using the generated data.

3. Failure Prediction
   The trained model predicts pipeline failure risk (HIGH or LOW).

## Technologies Used

Python
Scikit-learn
Pandas
NumPy

## Project Structure

GMIRE
│
├── src
│   ├── dataset_generator.py
│   ├── train_model.py
│   └── predict_failure.py

├── data
│   ├── pipe_data.csv
│   ├── road_data.csv
│   ├── water_data.csv
│   └── pipeline_model.pkl

## Author

Dhanushka K S
