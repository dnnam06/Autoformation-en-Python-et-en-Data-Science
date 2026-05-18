import streamlit as st
from functions_exo_1 import factorial_calculator_2

st.title("🧮 Factorial Calculator App")

# =========================================================
# USER INPUT
# =========================================================

# step=1 ensures that only integers can be selected
number = st.number_input(
    "Enter a positive integer (n):",
    min_value=0,
    max_value=100,
    value=5,
    step=1
)

# =========================================================
# DISPLAY RESULT
# =========================================================

if st.button("Calculate"):

    result = factorial_calculator_2(number)

    # Display formatted result
    st.metric(
        label=f"Result of {number}!",
        value=f"{result:,}"
    )

    # Show factorial expression for small numbers
    if number <= 10:
        expression = " * ".join(map(str, range(1, number + 1)))
        st.write(f"Explanation: ${number}! = {expression} = {result}$")

    else:
        st.info(
            "The number is quite large. "
            "Streamlit can still calculate it accurately, "
            "but the full multiplication expression will not be displayed."
        )

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("### Quick knowledge")

st.sidebar.write(
    "The factorial of n ($n!$) is the product "
    "of all positive integers from 1 to n."
)