from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="hybrid_search"
)

documents = [
    "FastAPI is used to build REST APIs.",
    "Python is a programming language.",
    "React is used for frontend development.",
    "Pydantic BaseModel validates incoming API data.",
    "SQL is used to manage databases."
]

ids = [f"doc_{i}" for i in range(len(documents))]

embeddings = model.encode(documents).tolist()

collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings
)

query = "Python framework for building APIs"

# 1. Keyword search
keyword_results = [
    doc for doc in documents
    if any(word.lower() in doc.lower() for word in query.split())
]

# 2. Semantic search
query_embedding = model.encode(query).tolist()

response = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

semantic_results = response["documents"][0]

print(semantic_results)

# 3. Combine results
hybrid_results = list(set(keyword_results + semantic_results))


print("Hybrid Search Results:")

for result in hybrid_results:
    print(result)