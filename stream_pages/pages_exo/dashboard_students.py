import streamlit as st
import time
from functions_students import alter_db, add_student
from functions_departments import get_departments
from functions_classrooms import get_classes
from functions_common import init_db

# ---------- INIT ----------
try:
    init_db()
except Exception as e:
    print("DB init error:", e)

alter_db("deleted_at", "DATETIME")

st.set_page_config(page_title="Quản lý sinh viên", layout="centered")

# ---------- MAIN FORM ----------
st.header("Student Add Form")

with st.form("my_students", clear_on_submit=True):

    # avoid errors (comment the 2 lines below to see the error)
    class_code = None
    classes_code = []

    departments = get_departments()
    
    if not departments:
        st.warning("No departments available")
    
    else:
        departments_code = []
        for department in departments:
            departments_code.append(department["code"])

        department_code = st.selectbox("Department Code", departments_code)
        department_code = str(department_code).zfill(3)

        classes = get_classes(department_code)

        if not classes:
            st.warning("No classes found for this department")

        else:
            for c in classes:
                classes_code.append(c["code"])

            class_code = st.selectbox("Class Code", classes_code, index=None, placeholder="Select a class")
            class_code = str(class_code).zfill(3)

    name = st.text_input("Student's name")
    age = st.number_input("Age", min_value=1, step=1)
    hometown = st.text_input("Hometown")

    submit = st.form_submit_button("Add student")

    if submit:
        if not (name and hometown):
            st.warning("Please fill all information")
        elif class_code not in classes_code:
            st.warning("Invalid class selected")
        else:
            add_student(
                department_code,
                class_code,
                name,
                age,
                hometown
            )
            st.success("Student added!")
            time.sleep(1)
            st.rerun()
