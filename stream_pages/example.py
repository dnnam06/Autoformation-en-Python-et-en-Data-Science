import streamlit as st

st.set_page_config(
    page_title="Management System",
    layout="wide"
)

# =========================================================
# DEFINE PAGES
# =========================================================

home_page = st.Page(
    page="views_example/home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

dashboard_page = st.Page(
    page="views_example/dashboard.py",
    title="Analytics Dashboard",
    icon=":material/bar_chart:"
)

# =========================================================
# MULTIPLE PAGE REFERENCES
# Different page variables can point to the same file
# but each page must have a unique URL path
# =========================================================

data_page_1 = st.Page(
    page="views_example/data.py",
    title="Data (Main Section)",
    icon=":material/data_check:",
    url_path="main-data"
)

data_page_2 = st.Page(
    page="views_example/data.py",
    title="Data (Tools Section)",
    url_path="tools-data"
)

# =========================================================
# NAVIGATION MENU
# =========================================================

pg = st.navigation(
    {
        "Main": [home_page, data_page_1],
        "Tools": [dashboard_page, data_page_2],
    }
)

pg.run()