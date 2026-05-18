import streamlit as st
import pandas as pd

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from students_analysis.functions_students import ranking

st.set_page_config(
    page_title="French Student Grade Management System",
    layout="wide"
)

st.title("🎓 French Student Grade Management & Analysis")

# =========================================================
# INITIAL SAMPLE DATA
# =========================================================

if 'df_students' not in st.session_state:
    data = {
        "Student ID": ["FR001", "FR002", "FR003", "FR004", "FR005"],
        "Full Name": ["Jean Dupont", "Marie Bernard", "Lucas Martin", "Emma Petit", "Thomas Robert"],
        "Age": [20, 21, 19, 22, 20],
        "Mathematics": [16.5, 12.0, 18.0, 9.5, 14.0],
        "Physics": [15.0, 13.5, 17.5, 10.0, 12.5],
        "Chemistry": [17.0, 11.5, 16.0, 8.5, 13.0],
        "Computer Science": [18.5, 14.0, 19.0, 11.0, 15.5],
        "English": [14.5, 16.0, 13.0, 12.0, 15.0],
        "Attendance (%)": [95, 88, 98, 72, 90]
    }
    st.session_state.df_students = pd.DataFrame(data)

# =========================================================
# DATA EDITOR
# =========================================================

st.subheader("1. Enter and Edit Student Grades")

st.info(
    "Tip: Double-click a cell to edit it. "
    "You can also add or remove rows dynamically."
)

edited_df = st.data_editor(
    st.session_state.df_students,
    num_rows="dynamic",
    use_container_width=True
)

# =========================================================
# ANALYSIS BUTTON
# =========================================================

if st.button("Calculate Results & Classification"):
    df_result = edited_df.copy()

    subjects = [
        "Mathematics",
        "Physics",
        "Chemistry",
        "Computer Science",
        "English"
    ]

    df_result["Average Grade"] = (
        df_result[subjects]
        .mean(axis=1)
        .round(2)
    )

    df_result["Mention"] = (
        df_result["Average Grade"]
        .apply(ranking)
    )

    df_result["Status"] = (
        df_result["Average Grade"]
        .apply(
            lambda x:
            "Passed" if x >= 10
            else "Failed"
        )
    )

    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    st.divider()

    st.subheader("📊 Analysis Results")

    st.dataframe(
        df_result.style.highlight_max(
            axis=0,
            subset=subjects,
            color="#d4edda"
        ),
        use_container_width=True
    )

    # =====================================================
    # QUICK STATISTICS
    # =====================================================

    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # BAR CHART
    # -----------------------------------------------------

    with col1:
        st.write("### Mention Statistics")
        st.bar_chart(
            df_result["Mention"]
            .value_counts()
        )

    # -----------------------------------------------------
    # BEST STUDENT
    # -----------------------------------------------------

    with col2:
        st.write("### Top Student")
        top_student = df_result.nlargest(1, "Average Grade")

        st.success(
            f"Best student: "
            f"**{top_student.iloc[0]['Full Name']}** "
            f"with an average grade of "
            f"**{top_student.iloc[0]['Average Grade']}**"
        )

    # =====================================================
    # EXTRA ANALYSIS
    # =====================================================

    st.divider()

    st.subheader("📈 Additional Analysis")

    # Average by subject
    subject_means = (
        df_result[subjects]
        .mean()
        .round(2)
    )

    st.write("### Subject Averages")

    st.bar_chart(subject_means)

    # Attendance analysis
    st.write("### Attendance Analysis")

    low_attendance = df_result[
        df_result["Attendance (%)"] < 80
    ]

    if not low_attendance.empty:
        st.warning("Students with low attendance detected.")

        st.dataframe(
            low_attendance,
            use_container_width=True
        )

    else:
        st.success("All students have acceptable attendance.")

    # =====================================================
    # DOWNLOAD CSV
    # =====================================================

    df_result.to_csv(
        "stream/exo_3/french_student_results.csv",
        index=False,
        encoding="utf-8-sig"
    )

    csv = (
        df_result
        .to_csv(index=False)
        .encode('utf-8-sig')
    )

    st.download_button(
        "📥 Download Results (CSV)",
        data=csv,
        file_name="french_student_results.csv",
        mime="text/csv"
    )