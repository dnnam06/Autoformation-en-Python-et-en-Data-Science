import streamlit as st
import time
from functions_departments import get_departments
from functions_classrooms import check_class_by_code, add_class

# ===== ADD CLASS =====
departments_for_class = get_departments()
st.header("➕ Add Class")

if departments_for_class:
    departments_code = []
    for department in departments_for_class:
        departments_code.append(department["code"])

    with st.form("add_class", clear_on_submit=True):
        dep = st.selectbox("Department", 
                           tuple(departments_code), 
                           index=None, 
                           placeholder="Select department...")
        new_class_code = st.text_input("Class code")
        new_class_name = st.text_input("Class name")

        submit_class = st.form_submit_button("Add class")

        if submit_class:
            if not new_class_code:
                st.warning("Class code cannot be empty.")
            elif check_class_by_code(dep, new_class_code):
                st.warning("Class existed.")
            else:
                add_class(dep, new_class_code, new_class_name)
                st.success(f"{new_class_code} has been added.")
                time.sleep(1)
                st.rerun()
else:
    st.info("There is no existing department.")

