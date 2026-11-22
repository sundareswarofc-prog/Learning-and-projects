from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app=FastAPI()
students=[]

@app.get("/")
def get_Home():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{id}")
def get_item(id:int):
    return{
        "item_id":id
    }

@app.get("/search")
def search(q:int,name:str):
    return{
        "q":q,
        "name":name
}

class Student(BaseModel):
    name:str
    age:int


@app.post("/body")
def post_data(student:Student):
    students.append(student)
    return{
        "message":"successfully created",
        "body":student
    }

@app.get("/students")
def get_student():
    return students

########## status code ###############

@app.get("/status",status_code=201)
def create_student():
    return {
        "message":"student created"
    }

######################################



########## Response models ###########

# Response modals are same as pydantic model but we can control the api response using this



class StudentCreate(BaseModel):
    name: str
    age: int
    marks: float


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    marks: float

@app.post("/createStudent",status_code=201,response_model=StudentResponse)
def create_student(student: StudentCreate):
    new_student = {
        "id": 1,
        "name": student.name,
        "age": student.age,
        "marks": student.marks,
        "internal_note": "Needs extra practice"
    }

    return new_student



################ HTTP exception #####################



students_1 = {
    1: {"id": 1, "name": "Arun"}
}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students_1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students_1[student_id]








