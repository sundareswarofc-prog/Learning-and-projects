from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()
class requestBody(BaseModel):
    question:str

app=FastAPI()

client=OpenAI()


@app.post("/ask")
def get_result(question:requestBody):
    response=client.responses.create(
        model="gpt-6-luna",
        input=question.question
    )

    return{
        "response":response.output_text
}


def ask_question(request):
    response=client.responses.create(
        model="gpt-6-luna",
        input=request,
        instructions="""  
            You are a Python programming teacher.
            Explain everything in beginner-friendly language.  
            Always provide simple examples.
            """,
    )
    return response.output_text

answer=ask_question("what is python")

print(answer)



