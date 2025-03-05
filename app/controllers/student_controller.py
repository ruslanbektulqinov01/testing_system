from ..models import Student
from ..schemes import ResponseMessage


def create_student_logic(student, db):
    student_email = db.query(Student).filter(Student.email == student.email).first()
    if student_email:
        return ResponseMessage(message="Student with this email already exists")
    new_student = Student(
        name=student.name,
        email=student.email
    )
    db.add(new_student)
    db.commit()
    return ResponseMessage(message="Student created successfully")


def get_student_logic(student_id, db):
    student = db.query(Student).filter(Student.id == student_id).first()
    return student

def delete_student_logic(student_id, db) -> ResponseMessage:
    student = db.query(Student).filter(Student.id == student_id).first()
    db.delete(student)
    db.commit()
    return ResponseMessage(message="Student deleted successfully")

def get_students_logic(db):
    students = db.query(Student).all()
    return students
