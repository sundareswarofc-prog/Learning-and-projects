1. Does an LLM automatically remember previous conversations?
        No, not automatically across independent API requests.

        Let's understand with an example.

        Imagine you send two questions to an LLM.
    
    First Request: 
        User: My name is Arun.
        AI: Nice to meet you, Arun!

    Second request:
        User: What is my name?
        AI: I don't know your name.


Feature             	     Manual history	                                 Conversations API
Store messages	           Python list/database	                                   OpenAI
Send previous context	        Manually	                                       Automatically through conversation
Multiple users	         Separate histories required	                           Separate conversation IDs
Persistence             	Depends on your storage	                               Server-side conversation storage
Control over history	       Full control                                     	Managed through API