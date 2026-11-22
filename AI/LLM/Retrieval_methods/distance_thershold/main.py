from sentence_transformers import SentenceTransformer
import chromadb


model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client=chromadb.PersistentClient(path="./chromadb")

collection=client.get_or_create_collection(
    name="thershold"
)

documents = [
    "AWS provides cloud computing services.",
    "Docker is used for containerization.",
    "React is used for frontend development.",
    "FastAPI is used to build backend APIs."
]

ids=[f"doc_{i}" for i in range(0,len(documents))]

metadatas=[{"source":doc.split()[0]} for doc in documents]

embeddings=model.encode(documents).tolist()

print(metadatas)

collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

query="What is python"

query_embeddings=model.encode(query)

response=collection.query(
    query_embeddings=query_embeddings,
    n_results=2
)

documents=response["documents"][0]
distances=response["distances"][0]
threshold = 0.5

for document,distance in zip(documents,distances):
       if distance <= threshold:
        print("Relevant:", document)
       else:
        print("Not relevant:", document)
        
### Here we can denote that the results are not relevant by setting a "thershold" value
