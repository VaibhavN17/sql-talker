import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

DB_PATH = "data/sales.db"
SCHEMA_INDEX_PATH = "schema_index"


def ensure_database():
    if not os.path.exists(DB_PATH):
        print("Database not found. Creating database...")
        subprocess.run(["python", "setup_db.py"], check=True)
    else:
        print("Database found.")


def ensure_schema_index():
    if not os.path.exists(SCHEMA_INDEX_PATH):
        print("Schema index not found. Building schema index...")
        subprocess.run(["python", "rag/ingest_schema.py"], check=True)
    else:
        print("Schema index found.")


def start_app():
    print("\nStarting SQL Talker...\n")
    subprocess.run(["python", "app.py"], check=True)


if __name__ == "__main__":
    ensure_database()
    ensure_schema_index()
    start_app()
