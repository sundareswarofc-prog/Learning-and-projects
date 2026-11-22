from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

response=client.responses.create(
    model="gpt-6-luna",
    input="Explain Python decorators",
    stream=True
)

# print(response.output_text)

for event in response:
    if event.type=="response.output_text.delta":
        print(event.delta,end="",flush=True)


# if event.type == "response.output_text.delta": -  This checks whether the current event contains a new piece of generated text.
# stream=True                                    - This tells the API to return events progressively instead of waiting for the complete response.
# event.delta                                    - contains the newly generated text.
# end=""                                         - prevents adding a new line after every chunk.
# flush=True                                     - displays output immediately.
