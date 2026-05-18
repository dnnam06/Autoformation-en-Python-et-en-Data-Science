import streamlit as st
import time
from functions_departments import check_department_by_code, add_department

st.header("⚙️ Department / Class Management")

with st.form("add_department", clear_on_submit=True):
    st.subheader("➕ Add Department")
    new_dep_code = st.text_input("Department code")
    new_dep_name = st.text_input("Department name")

    submit_dep = st.form_submit_button("Add department")

    if submit_dep:
        if not new_dep_code:
            st.warning("Department code cannot be empty")
        elif check_department_by_code(new_dep_code):
            st.warning("Department already exists")
        else:
            add_department(new_dep_code, new_dep_name)
            st.success(f"Department {new_dep_code} added successfully")
            time.sleep(1)
            st.rerun()