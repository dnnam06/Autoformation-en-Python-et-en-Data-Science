"""
=========================================================
STREAMLIT LEARNING NOTES
=========================================================
Run a Streamlit app with:

    streamlit run folder/file.py

=========================================================
1. DISPLAY TEXT AND DATA
=========================================================
"""

# import streamlit as st
# import pandas as pd

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

# st.write("My first dataframe")

# st.write(df)


"""
---------------------------------------------------------
st.write() vs print()
---------------------------------------------------------

print()
- Displays output in terminal

st.write()
- Displays output inside the web application
- Can display:
    - text
    - dataframe
    - charts
    - images

=========================================================
2. DISPLAY DATAFRAME
=========================================================
"""

# import streamlit as st
# import pandas as pd
# import numpy as np

# dataframe = pd.DataFrame(
#     np.random.randn(10, 5),
#     columns=["A", "B", "C", "D", "E"]
# )

# st.dataframe(dataframe)


"""
=========================================================
3. FULL SCREEN LAYOUT
=========================================================
"""

# import streamlit as st

# st.set_page_config(layout="wide")


"""
=========================================================
4. DATAFRAME STYLING
=========================================================
"""

# import streamlit as st
# import pandas as pd
# import numpy as np

# dataframe = pd.DataFrame(
#     np.random.randn(10, 5),
#     columns=["A", "B", "C", "D", "E"]
# )

# st.dataframe(
#     dataframe.style.highlight_between(
#         left=-0.5,
#         right=0.5,
#         color="#FFFF00"
#     )
# )


"""
=========================================================
5. LINE CHART
=========================================================
"""

# import streamlit as st
# import pandas as pd
# import numpy as np

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.line_chart(chart_data)


"""
=========================================================
6. MAP VISUALIZATION
=========================================================
"""

# import streamlit as st
# import pandas as pd
# import numpy as np

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon']
# )

# st.map(map_data)


"""
=========================================================
7. STREAMLIT WIDGETS
=========================================================

Widgets allow users to interact with the application.

Examples:
- slider 
- text_input 
- form
- button
- checkbox
- selectbox

=========================================================
8. SLIDER EXAMPLE
=========================================================
"""

# import streamlit as st

# x = st.slider("The square of x")

# st.write(x, "squared is", x * x)


"""
=========================================================
9. TEXT INPUT
=========================================================
"""

import streamlit as st

name = st.text_input("Your name", key='name') # key links the widget to session_state

st.write(name)

"""
=========================================================
10. SESSION STATE
=========================================================

Important concept:
Each interaction reruns the entire script.

Normal variables are reset after each rerun.

st.session_state is used to:
- store data
- keep memory
- persist values between reruns
- allow global access to widget values

=========================================================
11. SESSION STATE INITIALIZATION
=========================================================
"""

# import streamlit as st

# if 'count' not in st.session_state:
#     st.session_state.count = 0


"""
=========================================================
12. COUNTING EXAMPLE
Session State keeps the counting value between reruns. Without session_state, the counter would reset after each click
=========================================================
"""

# import streamlit as st

# if 'count' not in st.session_state:
#     st.session_state.count = 0

# increment = st.button("Add 1")

# if increment:
#     st.session_state.count += 1

# st.write(st.session_state.count)


"""
=========================================================
13. FORM
=========================================================

Forms group multiple widgets together.

The form only submits data when:
    
    st.form_submit_button() is pressed.

=========================================================
14. FORM EXAMPLE
=========================================================
"""

# import streamlit as st

# with st.form("my_form"):

#     age = st.number_input("Age")

#     submit = st.form_submit_button("Submit")

# if submit:
#     st.write(age)


"""
=========================================================
15. MINI PROJECT
=========================================================

Mini food management application:
- input food name
- input price
- save data
- display table
- save CSV
- use session state

=========================================================
16. COMPLETE MINI PROJECT
=========================================================
"""

import streamlit as st
import pandas as pd

st.title("Food Menu Application")

# =========================================================
# LOAD SESSION STATE
# =========================================================

if 'food_history' not in st.session_state:
    try:
        df = pd.read_csv("food_history.csv")
        st.session_state.food_history = (
            df.to_dict(orient='records')
        )
    except FileNotFoundError:
        st.session_state.food_history = []

# =========================================================
# FORM
# =========================================================

with st.form("food_form"):
    food_name = st.text_input("Food name")
    price = st.number_input("Price", min_value=0)
    submit = st.form_submit_button("Add food")

# =========================================================
# SAVE DATA
# =========================================================

if submit:
    st.session_state.food_history.append({
        "Food": food_name,
        "Price": price
    })

    df = pd.DataFrame(st.session_state.food_history)

    df.to_csv("stream/food_history.csv",index=False)

# =========================================================
# DISPLAY TABLE
# =========================================================

if st.session_state.food_history:
    df = pd.DataFrame(st.session_state.food_history)
    
    st.table(df)

    st.write(f"Total foods: {len(df)}")

"""
=========================================================
17. WHAT TO LEARN NEXT
=========================================================

Next Streamlit topics:
- sidebar
- columns
- tabs
- charts
- plotly
- file uploader
- caching
- database connection
- deployment

=========================================================
18. FINAL NOTES
=========================================================

Streamlit is extremely useful for:
- dashboards
- data analysis
- machine learning apps
- portfolio projects
- internal business tools

=========================================================
"""