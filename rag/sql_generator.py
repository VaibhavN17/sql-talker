from utils.prompts import SQL_PROMPT_TEMPLATE
from rag.retriever import retrieve_schema
from utils.gemini_llm import generate_text

def generate_sql(question: str) -> str:
    schema = retrieve_schema(question)

    prompt = SQL_PROMPT_TEMPLATE.format(
        schema=schema,
        question=question
    )

    sql = generate_text(prompt)

    # Safety: strip markdown if Gemini adds it
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql
