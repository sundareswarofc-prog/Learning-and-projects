from sentence_transformers import SentenceTransformer
import chromadb

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "AWS provides cloud computing services.",
    "Docker is used for containerization.",
    "React is used for frontend development.",
    "FastAPI is used to build backend APIs."
]

ids=["doc_1","doc_2","doc_3","doc_4"]

client=chromadb.PersistentClient(path="./chroma_db")

embeddings=model.encode(documents).tolist()

collection=client.get_or_create_collection(
    name="practice_task",
)

collection.upsert(
    embeddings=embeddings,
    ids=ids,
    documents=documents
)

query="Which technology helps me build REST APIs using Python?"

query_embeddings=model.encode(query).tolist()

response=collection.query(
    query_embeddings=[query_embeddings],
    n_results=3,
    include=["documents","distances"]  ### this finds the similarity distance 
)

print(response)

for item in response["documents"][0]:
    print(item)
    
# Assuming you configured cosine distance:
# - 0.12 = very similar.
# - 0.35 = less similar.
# - 0.78 = even less similar.
# Remember: ChromaDB returns cosine distance here, not cosine similarity. Smaller distance means a closer match.





