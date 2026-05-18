import streamlit as st
import math

from functions_students import restore_student, delete_student, get_total_expelled_students, get_expelled_student

# ------ version using dialog ------
st.title("🚫 Expelled students")

if "confirm_action" not in st.session_state:
    st.session_state.confirm_action = None

# multiple parameters can be added (for example, adding the year parameter as shown below)
@st.dialog("⚠️ Confirm action")
def confirm_dialog(action):

    student = action["student"]
    action_type = action["type"]
    year = action["xy"]

    st.write(
        f"Are you sure you want to **{action_type.upper()}** this student:"
        f"{year}"
    )
    st.info(
        f"{student['department_code']}{student['class_code']}{student['student_id']} - {student['name']}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Continue"):
            if action_type == "restore":
                restore_student(student["id"])

            if action_type == "delete":
                delete_student(student["id"])

            st.session_state.confirm_action = None
            st.rerun()
        
    with col2:
        if st.button("❌ Cancel"):
            st.session_state.confirm_action = None
            st.rerun()

if st.session_state.confirm_action:
    confirm_dialog(st.session_state.confirm_action)

total_expelled_students = get_total_expelled_students()

# --- Pagination ---
if "page" not in st.session_state:
    st.session_state.page = 1

students_per_page = 5
total_pages = max(1, math.ceil(total_expelled_students / students_per_page))

page = st.session_state.page

start = (page - 1) * students_per_page
end = start + students_per_page
students = get_expelled_student(start, end)

print(students)

for student in students:
    with st.expander(f"{student['id']} - {student['department_code']}{student['class_code']}{student['student_id']} - {student['name']}"):
        st.write(f"Department: {student['department_code']}")
        st.write(f"Class: {student['class_code']}")
        st.write(f"Age: {student['age']}")
        st.write(f"Hometown: {student['hometown']}")
        st.write(f"Expelled at: {student['deleted_at']}")

        if st.button("Restore", 
                     key=f"restore_{student['id']}"):
            st.session_state.confirm_action = {
                "type": "restore",
                "student": student, 
                "xy": 2026
            }
            st.rerun()

        if st.button("Delete", 
                     key=f"delete_{student['id']}"):
            st.session_state.confirm_action = {
                "type": "delete",
                "student": student,
                "xy": 2026
            }
            st.rerun()

st.divider()

cols = st.columns(total_pages + 2)

# Prev
with cols[0]:
    if st.button("⬅", disabled=page == 1):
        st.session_state.page -= 1
        st.rerun()

# Page numbers
for i in range(1, total_pages + 1):
    with cols[i]:
        if st.button(
            f"{i}",
            type="primary" if i == page else "secondary",
            key=f"page_{i}"
        ):
            st.session_state.page = i
            st.rerun()

# Next
with cols[-1]:
    if st.button("➡", disabled=page == total_pages):
        st.session_state.page += 1
        st.rerun()

    
