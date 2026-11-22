from sentence_transformers import SentenceTransformer
import chromadb

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client=chromadb.PersistentClient(path="./chromadb")
collection=client.get_or_create_collection(
      name="python_notes"
)

text=""

with open(".././python_notes.txt","r",encoding="utf-8") as f :
      text+=f.read()

chunk_size = 50
overlap = 10
chunks = []

for i in range(0,len(text),chunk_size-overlap):
      chunk=text[i:i+chunk_size]
      chunks.append(chunk)
     

ids=[f"chunk_{i}" for i in range(0,len(chunks))]

embeddings=model.encode(chunks).tolist()

print(chunks)
collection.upsert(
      ids=ids,
      embeddings=embeddings,
      documents=chunks
)




