from fastapi import APIRouter, HTTPException
from models import Student, StudentIn
from crud import create_student, get_students, update_student, delete_student

router = APIRouter()

@router.post("/students")
def add_student(student: StudentIn):
    new_student = Student(id=0, **student.dict())
    return create_student(new_student)

@router.get("/students")
def list_students():
    return get_students()

@router.put("/students/{student_id}")
def modify_student(student_id: int, student: StudentIn):
    updated = update_student(student_id, Student(id=student_id, **student.dict()))
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@router.delete("/students/{student_id}")
def remove_student(student_id: int):
    return delete_student(student_id)
