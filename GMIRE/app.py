# app.py
import streamlit as st

# Title
st.title("GMIRE – Infrastructure Risk Dashboard")

# Sample text
st.write("Welcome to the GMIRE dashboard!")

# Sample data directly in code (no CSV)
sample_data = {
    "Infrastructure": ["Road1", "Pipeline1", "Bridge1"],
    "Risk": [0.2, 0.5, 0.1]
}

# Display as table
st.subheader("Sample Infrastructure Risk Data")
st.table(sample_data)

# Bar chart
st.subheader("Infrastructure Risk Values")
st.bar_chart({"Risk": sample_data["Risk"]})