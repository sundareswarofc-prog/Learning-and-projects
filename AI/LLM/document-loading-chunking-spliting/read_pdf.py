from pypdf import PdfReader

reader = PdfReader("./pdf-sample_0.pdf")
text = ""
for page in reader.pages:
    text += (page.extract_text() or "") + "\n"

print(text)



text = """
Python is a programming language.
FastAPI is a Python framework.
ChromaDB stores embeddings.
RAG retrieves documents and generates answers.
"""

chunk_size = 50

chunks = [text[i:i+chunk_size]
    for i in range(0, len(text), chunk_size)
]

print(chunks)

for chunk in chunks:
    print(chunk)
    print("--------")