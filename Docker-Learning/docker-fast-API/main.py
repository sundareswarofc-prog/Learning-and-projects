from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first Dockerized FastAPI application!"}

@app.get("/students")
def get_students():
    return [
        {"id": 1, "name": "Sundar"},
        {"id": 2, "name": "John"}
    ]