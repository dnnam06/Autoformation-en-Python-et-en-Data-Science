import streamlit as st
import math
import time

from functions_students import restore_student, delete_student, get_total_expelled_students, get_expelled_student

# ------ version without dialog ------
st.title("🚫 Expelled students")

# How to display the success message outside the form or anywhere we want
msg = st.empty()

if 'is_restored' not in st.session_state:
    st.session_state.is_restored = False

if st.session_state.is_restored:
    msg.success("Student restored!")
    time.sleep(0.5)
    msg.empty()
    st.session_state.is_restored = False
    st.session_state.clicked = False

if 'is_deleted' not in st.session_state:
    st.session_state.is_deleted = False

if st.session_state.is_deleted:
    msg.success("Student deleted!")
    time.sleep(0.5)
    msg.empty()
    st.session_state.is_deleted = False
    st.session_state.clicked = False

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def on_click():
    st.session_state.clicked = True

total_expelled_students = get_total_expelled_students()

# --- Pagination ---
students_per_page = 10
total_pages = math.ceil(total_expelled_students/students_per_page)
page = st.number_input("Page", min_value=1, max_value=max(total_pages,1), value=1, step=1)

start = (page-1)*students_per_page
end = start + students_per_page
students = get_expelled_student(start, end)

for student in students:
    with st.expander(f"{student['id']} - {student['department_code']}{student['class_code']}{student['student_id']} - {student['name']}"):
        st.write(f"Department: {student['department_code']}")
        st.write(f"Class: {student['class_code']}")
        st.write(f"Age: {student['age']}")
        st.write(f"Hometown: {student['hometown']}")
        st.write(f"Expelled at: {student['deleted_at']}")

        if st.button("Restore", 
                     key=f"restore_{student['id']}", 
                     on_click=on_click, 
                     disabled=st.session_state.clicked):
            restore_student(student["id"])
            st.session_state.is_restored = True
            st.rerun()

        if st.button("Delete", 
                     key=f"delete_{student['id']}",  
                     on_click=on_click, 
                     disabled=st.session_state.clicked):
            delete_student(student["id"])
            st.session_state.is_deleted = True
            st.rerun()