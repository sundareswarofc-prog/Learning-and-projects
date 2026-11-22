Feature	                            Embedding model	                                        ChromaDB	                    FlashRank
Generates vectors	                    Yes	                                                   No	                          No
Stores vectors	                        No	                                                   Yes	                          No
Retrieves documents	                    No	                                                   Yes	                          No
Calculates relevance scores         	Similarity can be calculated from vectors	       Returns distances	              Yes
Reorders documents                     	No	                                                By vector distance	         By reranking score


1. What is FlashRank?
     FlashRank is a Python package that reranks documents based on how relevant they are to a user's question.