from sentence_transformers import SentenceTransformer
import chromadb

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chromadb")

collection = client.get_collection(name="python_notes")



print(collection)
query="What is Python used for?"

query_embeddings=model.encode(query).tolist()

# print(query_embeddings)

response=collection.query(
    query_embeddings=[query_embeddings],
    n_results=2
)

print(response["documents"][0])