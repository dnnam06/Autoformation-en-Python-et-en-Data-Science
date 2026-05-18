import streamlit as st 
from functions_exo_2 import *

st.set_page_config(page_title="Notes App", layout="centered")

st.title("📝 Notes App")

# Initialize database
init_db()

# Add a new column (deadline here) if it does not exist
alter_db('deadline', 'TEXT')

# =========================================================
# ADD NOTE FORM
# =========================================================

if "edit_id" not in st.session_state:
    with st.form("add_note_form", clear_on_submit=True):
        title = st.text_input(label="Title")
        content = st.text_area("Content")
        deadline = st.datetime_input("Finished before")
        submitted = st.form_submit_button("➕ Add note")

        if submitted:
            if title and content and deadline:
                add_note(title, content, deadline)
                st.success("Note added successfully!")
                st.rerun()

            else:
                st.warning("Please fill in all fields")

st.divider()

# =========================================================
# EDIT NOTE FORM
# =========================================================

if "edit_id" in st.session_state:
    note = get_row(st.session_state.edit_id)
    st.subheader("✏️ Edit note")
    
    with st.form("edit_form"):
        title = st.text_input("Title", value=note["title"])
        content = st.text_area("Content", value=note["content"])
        deadline = st.date_input( "Deadline", value=note["deadline"])
        submitted = st.form_submit_button("💾 Save")

        if submitted:
            update_row(note["id"], title, content, deadline)
            del st.session_state.edit_id
            st.success("Note updated successfully!")
            st.rerun()

# =========================================================
# DISPLAY NOTES
# =========================================================

st.subheader("📚 Notes List")

notes = get_notes()

if not notes:
    st.info("No notes available")

else:
    for note in notes:
        with st.expander(f"🗒 {note['title']} — {note['created_at']}"):
            st.write(note['content'])

            # Edit button
            if st.button("✏️ Edit", key=f"edit_{note['id']}"):
                st.session_state.edit_id = note["id"]
                st.rerun()

            # Delete button
            if st.button("❌ Delete", key=f"delete_{note['id']}"):
                delete_note(note['id'])
                st.rerun()