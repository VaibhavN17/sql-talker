from dotenv import load_dotenv
from rag.sql_generator import generate_sql
from db.execute_sql import execute_sql

load_dotenv()

print("SQL Talker is running. Type 'exit' to quit.")

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    try:
        sql = generate_sql(question)
        print("\nGenerated SQL:\n", sql)

        result = execute_sql(sql)
        print("\nResult:")
        for row in result:
            print(row)

    except Exception as e:
        print("Error:", e)
