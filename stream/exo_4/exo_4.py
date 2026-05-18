import streamlit as st
from functions_exo_4 import *

def add_student_callback():
    id = st.session_state.id
    name = st.session_state.name
    age = st.session_state.age
    hometown = st.session_state.hometown
    
    if get_row(id):
        st.warning("Please refill another valid ID.")
        st.session_state.id = ""
    else:
        if not (id and name and age and hometown):
            st.error("Please refill all information!")
        else:
            add_student(id, name, age, hometown)
            st.success("Student added!")
            # Reset form - reset both input keys and session_state
            st.session_state.id = ""
            st.session_state.name = ""
            st.session_state.age = 1
            st.session_state.hometown = ""

# --------------------------
# Part 2 : Codes for the app 
# --------------------------

# we need to bulid the layout for the app
st.set_page_config(page_title="Students list", layout="centered")
st.header("Form to add student")

# we have to init database to create the primary table 
init_db()

# Input fields with callbacks
st.text_input("Student's ID", value=st.session_state.get("id", ""), key="id")
st.text_input("Student's name", value=st.session_state.get("name", ""), key="name")
st.number_input("Student's age", value=st.session_state.get("age", 1), min_value=1, key="age")
st.text_area("Student's hometown", value=st.session_state.get("hometown", ""), key="hometown")

st.button("Add student", on_click=add_student_callback)

# layout for the students list
st.divider()
st.subheader("Students list")

# we have to store students we have (even no students) to a variable 
students = get_students()

# this is how the list works 
if not students: 
    st.info("There is no student in the list at the moment.")
else:
    for student in students:
        with st.expander(f"{student['id']} - {student['name']}"):
            st.write(f"Age: {student['age']}")
            st.write(f"Hometown: {student['hometown']}")
            if st.button(label="Delete", key=f"delete_{student['id']}"):
                delete_student(student['id'])
                st.rerun()