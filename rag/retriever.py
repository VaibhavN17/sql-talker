import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

INDEX_PATH = "schema_index"

# Lazy-initialized vectorstore; initialize on first use.
vectorstore = None

def _init_vectorstore():
    global vectorstore
    if vectorstore is not None:
        return

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Try loading existing index
    try:
        if os.path.exists(INDEX_PATH) and os.path.isdir(INDEX_PATH):
            vectorstore = FAISS.load_local(
                INDEX_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
            return
    except Exception:
        # fall through to rebuilding the index
        pass

    # Fallback: build index from DB schemas using ingest_schema.extract_schemas
    try:
        # import here to avoid circular imports at module import time
        from rag.ingest_schema import extract_schemas

        schemas = extract_schemas()
        if not schemas:
            raise RuntimeError("No schemas found to build index")

        vectorstore = FAISS.from_texts(schemas, embeddings)
        vectorstore.save_local(INDEX_PATH)
        return
    except Exception as e:
        raise RuntimeError(f"Failed to initialize vectorstore: {e}")


def retrieve_schema(question, k=2):
    _init_vectorstore()
    docs = vectorstore.similarity_search(question, k=k)
    return "\n\n".join(doc.page_content for doc in docs)
