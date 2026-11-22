from sentence_transformers import SentenceTransformer
import chromadb

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client=chromadb.PersistentClient(path="./chroma_db")

collection=client.get_or_create_collection(
    name="meta"
)


documents = [
    "Python supports object-oriented programming.",
    "FastAPI supports dependency injection.",
    "React is used to build user interfaces.",
    "FastAPI supports asynchronous endpoints."
]

embeddings=model.encode(documents)

ids = ["1", "2", "3", "4"]

metadatas = [
    {"category": "python"},
    {"category": "fastapi"},
    {"category": "react"},
    {"category": "fastapi"}
]

collection.upsert(
    embeddings=embeddings,
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

query="How does FastAPI handle asynchronous requests?"

query_embeddings=model.encode(query)

response=collection.query(
    query_embeddings=query_embeddings,
    where={
        "category":"fastapi"
    }
)

print(response)


############## another example 





metadatas_2 = [
    {"source": "python.pdf", "year": 2024},
    {"source": "fastapi.pdf", "year": 2025},
    {"source": "javascript.pdf", "year": 2023}
]

collection.upsert(
    embeddings=embeddings,
    ids=ids,
    documents=documents,
    metadatas=metadatas_2
)

response=collection.query(
    query_embeddings=query_embeddings,
   where={"year": {"$gte": 2024}}
)