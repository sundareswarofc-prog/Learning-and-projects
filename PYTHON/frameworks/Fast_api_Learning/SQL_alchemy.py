
from collections.abc import Generator

from fastapi import Depends, FastAPI, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Float, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session
from sqlalchemy.orm import mapped_column, sessionmaker


# 1. Database connection
DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# 2. SQLAlchemy database models
class Base(DeclarativeBase):
    pass


class StudentDB(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    marks: Mapped[float] = mapped_column(Float)


# Create the table if it does not exist
Base.metadata.create_all(bind=engine)


# 3. Pydantic request and response models
class StudentCreate(BaseModel):
    name: str
    age: int
    marks: float


class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    marks: float | None = None


class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    age: int
    marks: float


# 4. FastAPI application
app = FastAPI()


# 5. Database session dependency
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# 6. CREATE: add a student
@app.post("/students",response_model=StudentResponse,status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate,db: Session = Depends(get_db)):
    db_student = StudentDB(**student.model_dump())

    try:
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
    except Exception:
        db.rollback()
        raise

    return db_student


# 7. READ: get all students
@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students(db: Session = Depends(get_db)):
    statement = select(StudentDB)
    return db.scalars(statement).all()


# 8. READ: get one student
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.get(StudentDB, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# 9. UPDATE: change selected fields
@app.patch(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student_update: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.get(StudentDB, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updates = student_update.model_dump(exclude_unset=True)

    for field, value in updates.items():
        if value is None:
            raise HTTPException(
                status_code=422,
                detail=f"{field} cannot be null"
            )

        setattr(student, field, value)

    try:
        db.commit()
        db.refresh(student)
    except Exception:
        db.rollback()
        raise

    return student


# 10. DELETE: remove a student
@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.get(StudentDB, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    try:
        db.delete(student)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return Response(status_code=status.HTTP_204_NO_CONTENT)
