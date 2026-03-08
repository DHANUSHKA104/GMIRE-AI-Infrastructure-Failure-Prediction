import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import your model code if needed

st.title("GMIRE - Infrastructure Risk Dashboard")

# Example: show dataset from your data folder
df = pd.read_csv("data/sample_data.csv")
st.dataframe(df)

# Example chart
st.line_chart(df['value_column'])  # replace with actual column