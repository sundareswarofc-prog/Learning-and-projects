
from sentence_transformers import SentenceTransformer
from flashrank import Ranker, RerankRequest
import chromadb

# 1. Load embedding model
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Initialize FlashRank
ranker = Ranker()

# 3. Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="python_notes"
)

# 4. User question
query = "What is FastAPI used for?"

# 5. Generate query embedding
query_embedding = embedding_model.encode(query).tolist()

# 6. Retrieve documents from ChromaDB
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5,
    include=["documents", "metadatas"]
)

retrieved_documents = results["documents"][0]
retrieved_ids = results["ids"][0]

# 7. Prepare documents for FlashRank
passages = []

for doc_id, document in zip(retrieved_ids, retrieved_documents):
    passages.append({
        "id": doc_id,
        "text": document
    })

# 8. Create reranking request
request = RerankRequest(
    query=query,
    passages=passages
)

# 9. Rerank documents
ranked_results = ranker.rerank(request)

# 10. Print top 3 documents
for result in ranked_results[:3]:
    print("ID:", result["id"])
    print("Score:", result["score"])
    print("Document:", result["text"])
    print("------------------------")
