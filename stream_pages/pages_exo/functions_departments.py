from functions_common import get_conn

def add_department(code: str, name: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO departments (code, name)
        VALUES (?, ?)
    """, (code, name))
    conn.commit()
    conn.close()

def get_departments():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM departments
        ORDER BY name
    """)
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def check_departments():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM departments
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()

    if len(row) > 0:
        return True
    else: return False

def check_department_by_code(new_dep):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM departments WHERE code=? LIMIT 1""",
        (new_dep,)
    )
    row = cursor.fetchone()
    print("abc", row)
    conn.close()

    if row is not None:
        return True
    else: return False




