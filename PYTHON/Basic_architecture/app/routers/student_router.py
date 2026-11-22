from fastapi import APIRouter,Depends,Request
from pydantic import BaseModel
from app.controllers.student_controller import (create_student,get_students_controller,update_student_controller,remove_student)
from app.dependecies.student_dependency import get_student_service

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError

from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    SECRET_KEY,
    ALGORITHM
)

router = APIRouter()

class Student(BaseModel):
    name: str
    age: int
    course: str
    marks: float
    is_active: bool = True

class Student_details(Student):
    id:int




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Temporary user storage
fake_user = {
    "username": "arun",
    "hashed_password": hash_password("123456"),
    "role": "teacher"
}

def get_current_user(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        print(payload)

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return {
            "username": username,
            "role": payload.get("role")
        }

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

def require_teacher(user=Depends(get_current_user)):

    if user.get("role") != "teacher":
        raise HTTPException(
            status_code=403,
            detail="Teacher access required"
        )

    return user

@router.get("/profile")
def get_profile(user=Depends(get_current_user)):
    return user

@router.post("/login")
def login(request: Request,form_data = Depends(OAuth2PasswordRequestForm)):
    print(request.client.host,"hostname ")

    if form_data.username != fake_user["username"]:
        raise HTTPException(status_code=401, detail="Invalid username")

    if not verify_password(
        form_data.password,
        fake_user["hashed_password"]
    ):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({
        "sub": fake_user["username"],
        "role": fake_user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/py_students")
def add_student(student:Student_details):
    return {
        "message":"student added succesful",
        "data":student
    }

@router.post("/students",response_model=Student_details)
def add_student(student:Student):
    return create_student(student)

@router.get("/students")
def get_students(service=Depends(get_student_service)):
    return service["get_all"]()

@router.put("/students/{id}")
def update_student(id: int, name: str, age: int, user=Depends(require_teacher)):
     return update_student_controller(id, name, age)

@router.delete("/students/{id}")
def update_student(id: int,user=Depends(require_teacher)):
    if(user.get("role") == "admin"):
       return remove_student(id)
    else:
        raise HTTPException(status_code=401, detail="can't access")