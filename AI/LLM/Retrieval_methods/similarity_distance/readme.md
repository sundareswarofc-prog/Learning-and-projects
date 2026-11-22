1. what is the diffrence between cosine similarity and distance? 
    Similarity measures how alike two vectors are (higher = more alike). Distance measures how far apart they are (lower = more alike). They are two views of the same relationship, and for cosine they’re directly connected:

    *  cosine distance = 1 - cosine similarity *

    Cosine similarity          vs             cosine distance

    Range: -1 to 1	                            Range: 0 to 2
    1 = same direction (most similar)         0 = same direction (closest)
    0 = unrelated (perpendicular)             1 = unrelated
    -1 = opposite direction	                  2 = opposite direction
    Sort descending to find best matches	  Sort ascending to find best matches

    Example

    If two embeddings have cosine similarity 0.85, their cosine distance is 0.15.



  Keyword search	                  Semantic search
Searches matching                 words	Searches matching meaning
Exact terms matter                Similar meanings can match
Example: searching                FastAPI Example: searching Python API framework
   