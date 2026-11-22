1. what is chunk_overlap?
        * Chunk overlap means repeating a few characters from the previous chunk in the next chunk.
        * In RAG, splitting text into chunks can sometimes break important information between two chunks.

            For example:
            Without overlap
            Chunk 1: Python is a programming language used for

            Chunk 2: backend development and AI applications.

            The meaning may be split across chunks.

            With overlap
            Chunk 1: Python is a programming language used for

            Chunk 2: used for backend development and AI applications.

            The repeated words help preserve context.

        * This technique is called chunk overlap. We'll learn how to implement it in Python next.

