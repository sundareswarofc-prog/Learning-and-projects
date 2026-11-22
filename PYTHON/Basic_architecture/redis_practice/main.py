from fastapi import FastAPI
from redis_practice.redis_client import r

app = FastAPI()

@app.post("/students/{student_id}")
def add_student(student_id: int, name: str):

    r.set(f"student:{student_id}", name)

    return {
        "message": "Student stored in Redis"
    }


@app.get("/students/{student_id}")
def get_student(student_id: int):

    name = r.get(f"student:{student_id}")

    if name is None:
        return {"message": "Student not found"}

    return {
        "id": student_id,
        "name": name
    }
