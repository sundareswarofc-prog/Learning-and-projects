from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

app=FastAPI()

result=''

@app.get("/stream")
def get_result(input:str):

    def generate():
        response=client.responses.create(
            input=input,
            model="gpt-6-luna",
            stream=True
        )

        for event in response:
            if event.type=="response.output_text.delta":
                   yield event.delta

    result= StreamingResponse(
         generate(),
         media_type="text/plain"
    )
    return result

print(result)
