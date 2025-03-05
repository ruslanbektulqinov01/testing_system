from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemes import StudentScheme, ResponseMessage, StudentCreate
from fastapi import APIRouter, Depends
from app.controllers.student_controller import create_student_logic, get_student_logic, delete_student_logic, \
    get_students_logic

student_router = APIRouter()

@student_router.post("/students", response_model=ResponseMessage,
                     status_code=201,
                     summary="Create a student",
                     description="Create a student with a unique email")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student_logic(student, db)

@student_router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    return get_student_logic(student_id, db)

@student_router.get("/students", response_model=List[StudentScheme])
def get_students(db: Session = Depends(get_db)):
    return get_students_logic(db)

@student_router.delete("/students/{student_id}", response_model=ResponseMessage)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return delete_student_logic(student_id, db)
