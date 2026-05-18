import streamlit as st

st.title("🏠 Home Page")
st.write("Welcome to the multi-page application!")

# =========================================================
# USER INPUT
# =========================================================

# Get previous value from session_state
# If it does not exist, use an empty string
user_name = st.text_input(
    "Enter your name:",
    st.session_state.get("user_name", "")
)

# =========================================================
# SAVE DATA INTO SESSION STATE
# =========================================================

if user_name:
    st.session_state["user_name"] = user_name
    st.success(f"Name saved successfully: {user_name}")