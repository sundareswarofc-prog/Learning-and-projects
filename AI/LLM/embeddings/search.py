from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
   "JavaScript is used for frontend development.",
    "Python is popular for backend development.",
    "SQL is used to manage databases."
]

# Convert documents into embeddings
document_embeddings = model.encode(documents)

# User's search query
query = "Which language is useful for building backend applications?"

# Convert query into an embedding
query_embedding = model.encode(query)

# Compare query with all documents
scores = util.cos_sim(query_embedding, document_embeddings)[0]

# Find the most similar document
best_match = scores.argmax().item()

print("scores",scores,best_match)

print("Best matching document:", documents[best_match])
print("Similarity score:", scores[best_match].item())

sentence1 = "I love Python programming"
sentence2 = "Python is my favourite coding language"
sentence3 = "I like playing cricket"

embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)
embedding3 = model.encode(sentence3)

similarity1 = util.cos_sim(embedding1, embedding2)
similarity2 = util.cos_sim(embedding1, embedding3)
print(similarity1,"simi---")
print(similarity1.argmax().item(),similarity2.argmax().item())

print("Similarity 1:", similarity1.item())
print("Similarity 2:", similarity2.item())