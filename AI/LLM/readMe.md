1. What is LLM integration?
    LLM stands for Large Language Model.

    Examples of LLMs:
    - GPT
    - Claude
    - Gemini
    - Llama
    These models can understand and generate human-like text.

2. What is an LLM API?
    An API allows two applications to communicate with each other.

    For example, when you integrate OpenAI into Python:
    1. You create an API key.
    2. Your Python application sends a request using that key.
    3. OpenAI processes your input.
    4. OpenAI returns a response.
    5. Your Python application displays that response.
    An API key is used to authenticate your application. Keep it secret.

3. What is Prompt Engineering?
    Prompt engineering means writing clear instructions or questions to get better responses from an LLM.

    A prompt is simply the input you send to an AI model.

4. Types of prompts
     There are several common prompting techniques.

        A. Zero-shot prompting
             You give the model a task without providing examples.

             for example: prompt = """
                    Translate this sentence into Tamil:
                    Good morning, how are you?
                    """
        B. One-shot prompting
             You provide one example to show the model what you expect.

              For example: prompt = """
                                Convert text into uppercase.

                                Example:
                                Input: hello
                                Output: HELLO

                                Now convert:
                                Input: python programming
                                Output:
                                """

         c.Few-shot prompting

             You provide multiple examples before asking the actual question.

             for example: prompt = """
                            Classify the sentiment.

                            Example 1:
                            Text: I love this product.
                            Output: Positive

                            Example 2:
                            Text: This product is terrible.
                            Output: Negative

                            Example 3:
                            Text: The product is okay.
                            Output: Neutral

                            Now classify:
                            Text: The product is amazing.
                            Output:
                            """

         D. Role-based prompting

               This is an important technique when building AI applications.

                You can instruct the model to behave like a particular expert.

                for example:
                prompt = """
                            You are an experienced Python developer.

                            Explain Python decorators
                            to a beginner with a simple example.
                            """