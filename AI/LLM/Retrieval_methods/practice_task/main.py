from sentence_transformers import SentenceTransformer
import chromadb

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client=chromadb.PersistentClient(path=".././distance_thershold/chromadb")

collection=client.get_or_create_collection(
    name="practice_task"
)

documents = [
    "AWS provides cloud computing services.",
    "Docker is used for containerization.",
    "React is used for frontend development.",
    "FastAPI is used to build backend APIs.",
    "JavaScript is used for frontend development.",
    "Python is popular for backend development.",
    "SQL is used to manage databases."
]

ids=[f"doc_{i}" for i in range(0,len(documents))]

metadatas=[{"source":doc.split()[0]} for doc in documents]

embeddings=model.encode(documents).tolist()

query="what is AWS"

query_embeddings=model.encode(query).tolist()

collection.upsert(
    ids=ids,
    metadatas=metadatas,
    documents=documents,
    embeddings=embeddings
)

response=collection.query(
    query_embeddings=query_embeddings,
    n_results=1
)

retrieved_documents=response["documents"][0]
distances=response["distances"][0]

threshold=0.5
found = False

for distance,document in zip(distances,retrieved_documents):
    print(distance)
    if distance <= threshold:
        print(distance, "-----------", document)
        found = True

if not found:
    print("No relevant documents found")

