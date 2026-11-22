from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import chromadb
from openai import OpenAI

load_dotenv()

AI_bot=OpenAI()

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client=chromadb.PersistentClient(path="./rag_db")

collection=client.get_or_create_collection(
    name="python_doc"
)

ids=["doc_1","doc_2","doc_3","doc_4"]

documents = [
    "FastAPI is a Python framework used to build APIs.",
    "Python supports object-oriented programming.",
    "ChromaDB is a vector database used to store embeddings.",
    "RAG retrieves relevant documents and provides them to an LLM."
]

doc_embeddings=model.encode(documents).tolist()

query="How can I build APIs using Python?"

query_embeddings=model.encode(query)

collection.upsert(
    documents=documents,
    ids=ids,
    embeddings=doc_embeddings
)

response=collection.query(
    query_embeddings=[query_embeddings],
    n_results=2
)

print("response",response)

context="\n".join(response["documents"][0])

print("context", context)

prompt=f"""Answer the question using only the context below.

If the answer is not available in the context,
say that you don't have enough information.

Context:
{context}

Question:
{query}"""

result=AI_bot.responses.create(
        model="gpt-6-luna",
        input=prompt,
)

print(result.output_text)













