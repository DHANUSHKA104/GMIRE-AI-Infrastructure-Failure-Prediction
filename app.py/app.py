import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("GMIRE - Infrastructure Risk Dashboard")

# Load example dataset
try:
    df = pd.read_csv("../data/sample_data.csv")  # Replace with your actual CSV file
    st.dataframe(df)
    st.line_chart(df[df.columns[1]])  # Example: chart second column
except Exception as e:
    st.write("Dataset not found or error:", e)

st.write("This is your GMIRE dashboard prototype.")