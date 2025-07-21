from database import load_students, save_students
from models import Student
from logger import log_operation

@log_operation
def create_student(student: Student):
    students = load_students()
    student.id = students[-1]["id"] + 1 if students else 1
    students.append(student.dict())
    save_students(students)
    return student

@log_operation
def get_students():
    return load_students()

@log_operation
def update_student(student_id: int, updated: Student):
    students = load_students()
    for student in students:
        if student["id"] == student_id:
            student["name"] = updated.name
            student["age"] = updated.age
            student["marks"] = updated.marks
            save_students(students)
            return student
    return None

@log_operation
def delete_student(student_id: int):
    students = load_students()
    filtered = [s for s in students if s["id"] != student_id]
    save_students(filtered)
    return {"message": "Deleted if existed"}
