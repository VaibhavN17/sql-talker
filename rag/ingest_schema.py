import sqlite3
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

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

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(schemas, embeddings)
    vectorstore.save_local(INDEX_PATH)

    print("Schema index created successfully")

if __name__ == "__main__":
    ingest()
