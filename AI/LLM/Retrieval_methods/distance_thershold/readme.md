What is Distance Thershold?

    Imagine a user asks:

    "What is the capital of France?"

    But your database only contains Python and FastAPI documents.

    ChromaDB might still return the closest available documents, even though none is relevant.

    We can use a distance threshold to reject weak matches.