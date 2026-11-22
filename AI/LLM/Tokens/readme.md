1. What is a token?
    A token is a small unit of text that an LLM uses to process information.

    A token can be:
    - A complete word.
    - Part of a word.
    - A punctuation mark.
    - A space or other text representation.

    For example: I love python programming!

       Notice that one word is not always equal to one token.

      For example, a longer or uncommon word might be split into multiple tokens.

2. What is tokenization? 

     Tokenization is the process of converting text into tokens that an LLM can understand.

     The general process:
                    Input text ("I love Python" ) -> Tokenizer (Splits text into token units) ->  Token IDs (Each token maps to a numerical ID) -> LLM processing (The model processes the numerical representation)

      Because neural networks work with numerical data, not raw text directly.
     
        Type	           Meaning
        Characters	    Individual letters, spaces and punctuation
        Words	          Python, is, awesome
        Tokens	          Units produced by the tokenizer

3. Why are tokens important in LLM APIs?

      There are three major reasons :
            * API cost
            * Context Window
            * Response Length 
     
      API cost :

         Many LLM APIs charge based on token usage.

            For example, imagine a hypothetical pricing model:

            Token type	        Cost per 1 million tokens
            Input tokens        	    $2
            Output tokens        	    $8
        
      Context Window : 

          Every LLM has a maximum amount of input and output it can handle in a request.

            This limit is called the context window.

            For example, imagine a model has a 10,000-token context window.

            If you send:
            - System instructions: 1,000 tokens
            - Conversation history: 5,000 tokens
            - Current question: 1,000 tokens
            Total input = 7,000 tokens.

            That leaves approximately 3,000 tokens for additional context and generated output, subject to the model's specific limits.

      Response length : 

         The more output tokens a model generates, the longer its response can be and the more output-token charges it may incur.



