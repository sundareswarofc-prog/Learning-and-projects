from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

students=[]
student_id=1

class CreateStudent(BaseModel):
   name:str 
   age:int
   dept:str

class Student(CreateStudent):
   id:int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    dept: Optional[str] = None

@app.get("/view")
def view_students():
    if not students:
      raise HTTPException(status_code=201,detail="No Students Found")
    return students

@app.post("/add",status_code=status.HTTP_201_CREATED)
def add_student(student:CreateStudent):
   global student_id
   temp=Student(id=student_id,**student.model_dump())
   students.append(temp.model_dump())
   student_id+=1
   return {
      "message": "students added successfully",
      "data":student.model_dump()
   }

@app.delete('/student/{id}')
def delete_student(id:int):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {
               "message":"Student deleted successfully"
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

@app.patch("/student/{id}")
def update_student(id: int, student_update: UpdateStudent):
    updates = student_update.model_dump(exclude_unset=True)
    print(updates)
    if not updates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields provided to update"
        )
    for student in students:
        if student["id"] == id:
            student.update(updates)
            return {
                "message": "Student updated successfully",
                "data": student
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")



      
   
   