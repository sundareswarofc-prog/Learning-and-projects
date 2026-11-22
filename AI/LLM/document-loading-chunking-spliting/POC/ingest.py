from read_pdf import all_chunks
from sentence_transformers import SentenceTransformer
import chromadb

client=chromadb.PersistentClient(path="./vector_db")

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

text=[x["text"] for x in all_chunks]

embeddings=model.encode(text).tolist()

ids=[f"doc_{i}" for i in range(len(text))]

collection=client.get_or_create_collection(
    name="test_questions"
)
metadata=[{"source":item["source"]} for item in all_chunks]
# print(metadata)

collection.upsert(
    documents=text,
    ids=ids,
    embeddings=embeddings,
    metadatas=metadata
)

query="what is Tokenization"

query_embeddings=model.encode(query)

response=collection.query(
    query_embeddings=query_embeddings,
    n_results=2
)

print(response)

# print(response["documents"][0])









