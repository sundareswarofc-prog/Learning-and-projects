1. What is Top-K retrieval?

        Suppose you ask:

        "What is FastAPI?"

        ChromaDB may contain 100 document chunks.

        You don't need all 100 results. You only need the most relevant ones.

        That's what n_results controls.


        Here, n_results=3 means retrieve the three closest matching documents.

        This is commonly called Top-K retrieval.