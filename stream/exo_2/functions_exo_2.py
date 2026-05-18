import sqlite3
from datetime import datetime


def get_connection():
    conn = sqlite3.connect(
        "stream/exo_1/notes.db",
        check_same_thread=False
    )

    # safer because values can be accessed by column names instead of column indexes
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT
        )          
    """)
    conn.commit()
    conn.close()

def alter_db(new_column: str, type_column: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(notes)")

    rows = cursor.fetchall() # Lưu vào rows để tránh lỗi (có thể xoá đi để biết thêm chi tiết)
    columns = [row[1] for row in rows]

    if new_column not in columns:
        cursor.execute(f"ALTER TABLE notes ADD COLUMN {new_column} {type_column}")

    conn.commit()
    conn.close()

def add_note(title, content, deadline):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO notes (title, content, deadline, created_at) 
        VALUES (?, ?, ?, ?)""",
        (title, content, deadline, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()

# SELECT queries do not modify the database, so commit() is not necessary
# commit() -> INSERT, UPDATE, DELETE...
def get_notes():
    conn = get_connection()
    cursor = conn.cursor()
    # order of columns is not important while SELECT
    cursor.execute(
        "SELECT id, title, content, deadline, created_at FROM notes ORDER BY id DESC"
    )
    rows = cursor.fetchall()
    # close before return
    conn.close()
    return rows

def get_row(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM notes WHERE id = {id}"
    )
    row = cursor.fetchone()
    conn.close()
    return row

def update_row(id: int, title: str, content: str, deadline: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            UPDATE notes
            SET title = ?, content = ?, deadline = ?
            WHERE id = ?
        """, (title, content, deadline, id))
    conn.commit()
    conn.close()
    
def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()