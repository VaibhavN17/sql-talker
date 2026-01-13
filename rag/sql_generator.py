from langchain_openai import ChatOpenAI
from utils.prompts import SQL_PROMPT_TEMPLATE
from rag.retriever import retrieve_schema

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

def generate_sql(question):
    schema = retrieve_schema(question)

    prompt = SQL_PROMPT_TEMPLATE.format(
        schema=schema,
        question=question
    )

    return llm.predict(prompt).strip()
