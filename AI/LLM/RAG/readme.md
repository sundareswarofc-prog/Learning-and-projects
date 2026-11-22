1. What is RAG?

    RAG stands for Retrieval-Augmented Generation.

    It means retrieving relevant information from your own documents and giving that information to an LLM so it can generate an answer.

    Imagine you have a document containing information about your company's leave policy.

    A user asks:
    How many days of annual leave do employees get?

    A normal LLM might not know your company's policy.

    But with RAG, your application can search your company documents, retrieve the relevant information, and give it to the LLM.


Normal LLM	                                                                      RAG
Answers using its learned knowledge and supplied prompt	                  Answers using its learned knowledge and retrieved context
Doesn't automatically know your private documents	                     Can retrieve information from your documents
No retrieval step	                                                           Has a retrieval step
General-purpose chatbot	                                                    Can be a document-based chatbot

