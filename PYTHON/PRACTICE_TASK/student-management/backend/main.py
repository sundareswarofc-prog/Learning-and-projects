
import os
from contextlib import asynccontextmanager
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from sqlalchemy import String, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    sessionmaker,
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise RuntimeError("Set DATABASE_URL in backend/.env")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    course: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)


class StudentInput(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    course: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=16, le=100)


class StudentOutput(StudentInput):
    id: int
    model_config = ConfigDict(from_attributes=True)


def get_session():
    with SessionLocal() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(title="Student Management API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,


    
    allow_origins=["http://localhost:3000"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Student Management API is running"}


@app.get("/api/students", response_model=list[StudentOutput])
def list_students(
    session: SessionDep,
    search: Annotated[str | None, Query(max_length=100)] = None,
):
    statement = select(Student).order_by(Student.id.desc())

    if search and search.strip():
        term = f"%{search.strip()}%"
        statement = statement.where(
            Student.name.ilike(term)
            | Student.email.ilike(term)
            | Student.course.ilike(term)
        )

    return session.scalars(statement).all()


@app.get("/api/students/{student_id}", response_model=StudentOutput)
def get_student(student_id: int, session: SessionDep):
    student = session.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.post(
    "/api/students",
    response_model=StudentOutput,
    status_code=201,
)
def create_student(data: StudentInput, session: SessionDep):
    print(data,data)
    student = Student(**data.model_dump())
    session.add(student)

    try:
        session.commit()
        session.refresh(student)
    except IntegrityError as exc:
        session.rollback()
        raise HTTPException(
            status_code=409, detail="Email already exists"
        ) from exc

    return student


@app.put("/api/students/{student_id}", response_model=StudentOutput)
def update_student(
    student_id: int,
    data: StudentInput,
    session: SessionDep,
):
    student = session.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    for field, value in data.model_dump().items():
        setattr(student, field, value)

    try:
        session.commit()
        session.refresh(student)
    except IntegrityError as exc:
        session.rollback()
        raise HTTPException(
            status_code=409, detail="Email already exists"
        ) from exc

    return student


@app.delete("/api/students/{student_id}", status_code=204)
def delete_student(student_id: int, session: SessionDep):
    student = session.get(Student, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    session.delete(student)
    session.commit()
    return Response(status_code=204)
