
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
load_dotenv()

# client = OpenAI()

# response = client.embeddings.create(
#     model="gpt-6-luna",
#     input="Python is a programming language"
# )

# embedding = response.data[0].embedding

# print(embedding)

# print("Vector dimensions:", len(embedding))

#### used with openAI but it is paid only so I used sentence transformer 

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentence=[
    "I love python",
    "python is a easiest language.",
     "The weather is very hot today"
]

embeddings=model.encode(sentence)

similarities = model.similarity(embeddings, embeddings)

print("similarities",similarities)

