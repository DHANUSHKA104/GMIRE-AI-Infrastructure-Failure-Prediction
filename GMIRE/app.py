# app.py
import streamlit as st
import pandas as pd

# Title
st.title("GMIRE – Infrastructure Risk Dashboard")

# Load CSV from data folder
df = pd.read_csv("data/sample_data.csv")  # must match your folder structure

# Show dataframe
st.subheader("Sample Infrastructure Data")
st.dataframe(df)

# Simple bar chart
st.subheader("Infrastructure Risk Values")
st.bar_chart(df.set_index("name")["value"])