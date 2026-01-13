from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

INDEX_PATH = "schema_index"

vectorstore = FAISS.load_local(
    INDEX_PATH,
    OpenAIEmbeddings(),
    allow_dangerous_deserialization=True
)

def retrieve_schema(question, k=2):
    docs = vectorstore.similarity_search(question, k=k)
    return "\n\n".join(doc.page_content for doc in docs)
