import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Dashboard")

# =========================================================
# GET USER NAME FROM SESSION STATE
# =========================================================

# Retrieve the username from session_state
# If it does not exist, use "Guest" as default value
name = st.session_state.get("user_name", "Guest")

st.subheader(f"Data for: {name}")

# =========================================================
# GENERATE SAMPLE DATA
# =========================================================

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(chart_data)