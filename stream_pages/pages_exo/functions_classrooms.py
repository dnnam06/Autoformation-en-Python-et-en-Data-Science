from functions_common import get_conn

def add_class(department_code: str, code: str, name: str):
    if check_class_by_code(department_code, code):
        return False
    
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO classes (department_code, code, name)
        VALUES (?, ?, ?)
    """, (department_code, code, name))
    conn.commit()
    conn.close()

def get_classes(department_code: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM classes
        WHERE department_code = ?
        ORDER BY CAST(code AS INTEGER)
    """, (department_code,))
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows

def check_classes():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 1 FROM classes
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()

    if row is not None:
        return True
    else: return False

def check_class_by_code(dep_code, class_code):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM classes WHERE department_code=? AND code=? LIMIT 1""",
        (dep_code, class_code,)
    )
    row = cursor.fetchone()
    conn.close()

    if row is not None:
        return True
    else: return False