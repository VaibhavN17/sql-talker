import sqlite3
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os

DB_PATH = "data/sales.db"
INDEX_PATH = "schema_index"

def extract_schemas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT sql FROM sqlite_master
    WHERE type='table' AND sql IS NOT NULL;
    """)

    schemas = [row[0] for row in cursor.fetchall()]
    conn.close()
    return schemas

def ingest():
    schemas = extract_schemas()
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_texts(schemas, embeddings)
    vectorstore.save_local(INDEX_PATH)

    print("Schema index created")

if __name__ == "__main__":
    ingest()
