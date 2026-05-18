import sqlite3

# --------------------------------------
# Part 1 : Functions to help run the app
# --------------------------------------

# we have to get connection first
def get_conn():
    conn = sqlite3.connect(
        "stream/exo_4/students.db",
        check_same_thread=False
    )
    conn.row_factory = sqlite3.Row
    return conn

# we have to init database also
def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            hometown TEXT NOT NULL
        )          
    """)
    conn.commit()
    conn.close()

# we need a function to add student to our list
def add_student(id: str, name: str, age: int, hometown: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (id, name, age, hometown) 
        VALUES (?, ?, ?, ?)""",
        (id, name, age, hometown)
    )
    conn.commit()
    conn.close()

# we need a function to store students 
def get_students():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, age, hometown 
        FROM students 
        ORDER BY CAST(id AS INTEGER) ASC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

# we may need a function that helps remove the student we want 
def delete_student(id: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

def get_row(id: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()
    return row