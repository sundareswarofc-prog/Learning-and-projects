1. What problem does a Vector Database solve?
     In our previous exercise, we stored embeddings in a Python variable:
       document_embeddings = model.encode(documents)

       This works, but imagine you have:
        - 10,000 documents
        - 100,000 documents
        - 1 million documents

       Keeping all embeddings in Python variables becomes difficult. Also, when your program stops, those variables disappear.

       A Vector Database helps us store embeddings permanently and retrieve similar documents efficiently.

2. What is ChromaDB?
    ChromaDB is a vector database that lets you store and search numerical embeddings.

    It can store three important things:
            Data	      Example
            ID	           doc1
            Document	Python is a programming language
            Embedding	[0.12, 0.45, -0.21, ...]

    You can also store metadata, such as category, author, or document source.