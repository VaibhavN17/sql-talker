import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT,
    amount INTEGER,
    sale_date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

users = [
    (1, "John", "Sales Rep"),
    (2, "Alice", "Sales Rep"),
    (3, "Bob", "Manager")
]

sales = [
    (1, 1, "Laptop", 1200, "2025-12-01"),
    (2, 1, "Mouse", 50, "2025-12-02"),
    (3, 2, "Keyboard", 100, "2025-12-03"),
    (4, 2, "Monitor", 300, "2025-12-05"),
    (5, 1, "Laptop", 1200, "2025-12-10")
]

cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users)
cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?)", sales)

conn.commit()
conn.close()

print("Database created at data/sales.db")
