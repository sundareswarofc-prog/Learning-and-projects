from sentence_transformers import SentenceTransformer
import numpy as np

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Python is a programming language",
    "FastAPI is a Python web framework",
    "React is a JavaScript library",
    "Machine learning is a branch of AI"
]

doc_vectors =model.encode(documents)

# result_1_vector=[x for x in result_1]

question = "Which framework can I use with Python?"

question_vector=model.encode(question)

def cos_similarity(a,b):
    return np.dot(a,b)/(
        np.linalg.norm(a)*np.linalg.norm(b)
    )

scores = []

for index,item in enumerate(doc_vectors):
       score= cos_similarity(
             question_vector,
             item
       )
       scores.append((score,documents[index]))



print(scores.sort(reverse=True))