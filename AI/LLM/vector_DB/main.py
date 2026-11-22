
from sentence_transformers import SentenceTransformer
import chromadb



# Load free embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Create a persistent ChromaDB database
client = chromadb.PersistentClient(path="./chroma_db")

# Create a collection
collection = client.get_or_create_collection(
    name="python_documents",
    metadata={"hnsw:space": "cosine"}
)

# Our documents
documents = [
    "Python is a programming language.",
    "FastAPI is a Python web framework.",
    "React is a JavaScript library.",
    "SQL is used to manage databases."
]

ids = ["doc1", "doc2", "doc3", "doc4"]

# Generate embeddings
embeddings = model.encode(documents).tolist()
print(embeddings,"embeddings")

# Store documents and embeddings
collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings
)

print("Documents stored successfully!")

query="Which framework is useful for Python backend development?"
query_embeddings=model.encode(query)

response=collection.query(
    query_embeddings=query_embeddings,
    n_results=2
)

print("Matching documents:",response)


for document in response["documents"][0]:
    print(document)

print("Distances:", response["distances"][0])