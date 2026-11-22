1. What is document loading?
     Document loading means reading content from external files and converting it into text that our application can process.

2. What is chunking?
     Imagine your PDF contains 10,000 words.

     If you send the entire document to an embedding model at once, it may exceed the model's input limit and make retrieval less precise.

     Instead, divide the document into smaller pieces called chunks.

     Original document
          Python is a programming language. FastAPI is a Python framework. ChromaDB stores embeddings. RAG retrieves documents and generates answers.

          After chunking
          Chunk 1

          Python is a programming language.


          Chunk 2

          FastAPI is a Python framework.


          Chunk 3

          ChromaDB stores embeddings.


          Chunk 4

          RAG retrieves documents and generates answers.

3. Why do we use chunk in RAG?
     Imagine you have a document containing 1,000 characters.

     You don't want to create one embedding for the entire document. Instead, you split it into smaller chunks.

4. What is chunk overlap?
     Chunk overlap means repeating a few characters from the previous chunk in the next chunk.

     For example, suppose:

          In RAG, splitting text into chunks can sometimes break important information between two chunks.

          For example:
          Without overlap
          Chunk 1: Python is a programming language used for

          Chunk 2: backend development and AI applications.

          The meaning may be split across chunks.

          With overlap
          Chunk 1: Python is a programming language used for

          Chunk 2: used for backend development and AI applications.