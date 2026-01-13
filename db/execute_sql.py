import sqlite3

DB_PATH = "data/sales.db"

def execute_sql(sql):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    conn.close()
    return rows
