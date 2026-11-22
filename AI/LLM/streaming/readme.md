1. What is streaming?
        Normally, when you call an LLM API, it generates an answer and returns the complete response.

        But streaming works differently.

        It sends the generated response in small pieces as the model produces them.

        Let's understand with an example.

                Normal response:

                    User: Explain Python.
                    AI response---
                    Complete

                    Python is a high-level programming language. It is easy to learn and widely used in web development, automation, data science and AI.
                    The user waits until the complete answer is generated.

                Streaming response:

                    AI response
                    Streaming---

                    Python

                    Python is a

                    Python is a high-level

                    Python is a high-level programming language.
                    Illustrative sequence of incoming text chunks.
                    The user starts seeing the answer before the model finishes generating it.     

2. Normal vs Streaming

Normal response                                        	Streaming response
Waits for the complete answer	                     Receives chunks progressively
Simple implementation                                	Requires stream handling
Good for short responses	                                 Good for long responses
User waits longer to see text                           	User sees text sooner