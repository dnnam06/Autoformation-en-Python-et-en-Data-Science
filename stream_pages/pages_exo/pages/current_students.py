import streamlit as st
import math
import time

from functions_students import get_active_students, expel_student

st.title("🎓 Currently Enrolled Students")

if "confirm_action" not in st.session_state:
    st.session_state.confirm_action = None 

@st.dialog("⚠️ Confirm action")
def confirm_dialog(action):
    student = action["student"]
    action_type = action["type"]

    st.write(
        f"Are you sure you want to **{action_type.upper()}** this student:"
    )
    st.info(
        f"{student['department_code']}{student['class_code']}{student['student_id']} - {student['name']}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Continue"):
            if action_type == "expel":
                expel_student(student["id"])

            st.session_state.confirm_action = None
            st.rerun()

    with col2:
        if st.button("❌ Cancel"):
            st.session_state.confirm_action = None
            st.rerun()

if st.session_state.confirm_action:
    confirm_dialog(st.session_state.confirm_action)

students = get_active_students()

# --- Pagination ---
students_per_page = 10
total_pages = math.ceil(len(students)/students_per_page)
page = st.number_input("Page", min_value=1, max_value=max(total_pages,1), value=1, step=1)

start = (page-1)*students_per_page
end = start + students_per_page

for student in students[start:end]:
    with st.expander(f"{student['id']} - {student['department_code']}{student['class_code']}{student['student_id']} - {student['name']}"):
        st.write(f"Department: {student['department_code']}")
        st.write(f"Class: {student['class_code']}")
        st.write(f"Age: {student['age']}")
        st.write(f"Hometown: {student['hometown']}")

        if st.button("Expel", key=f"expel_{student['id']}"):
            # st.success("Student expelled!")
            st.session_state.confirm_action = {
                "type": "expel",
                "student": student
            }
            time.sleep(0.5)
            st.rerun()
