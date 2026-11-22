1. What are embeddings?

    An embedding is a numerical representation of text.
    In simple words, embeddings convert text into a list of numbers called a vector.

    For example: Python is a programming language.
    An embedding model converts this text into something like: [0.21, 0.54, -0.12, 0.87, 0.33]

2. What is a vector?
    A vector is simply a list of numbers.

    For example:
    vector = [10, 20, 30, 40]

    Here:
    - 10 is the first dimension.
    - 20 is the second dimension.
    - 30 is the third dimension.
    - 40 is the fourth dimension.
    An embedding is a vector containing numerical values learned by an embedding model.

3. How do embeddings work?

   Input text -> Embedding model (Converts text into numerical representation) -> Embedding vector [0.21, 0.54, -0.12, ...] -> Similarity search (Finds semantically similar text)


   Concept                      	Meaning
  Embedding	                    Numerical representation of text
  Vector	                         List of numbers
  Embedding model              	Converts text into vectors
  Semantic similarity          	Measures similarity in meaning
  Cosine similarity	            Compares vector directions
  Semantic search	               Finds relevant content using embeddings