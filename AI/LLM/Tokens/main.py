import tiktoken
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

text="I Love python programming"

encoding=tiktoken.get_encoding("cl100k_base")

tokens=encoding.encode(text)


print("Token IDs:", tokens)

print("Token count:", len(tokens))

client = OpenAI()

response=client.responses.create(
    model="gpt-6-luna",
    input="What is python"
)

print("response:", response.output_text)
print("Input Tokens:", response.usage.input_tokens)
print("Output Tokens:", response.usage.output_tokens)
print("Total_Tokens:", response.usage.total_tokens)



 