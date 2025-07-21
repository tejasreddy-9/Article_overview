import json
import os

FILE_NAME = "students.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def load_students():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_students(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

@log_operation
def create_student(name, age, marks):
    students = load_students()
    student = {
        "id": students[-1]["id"] + 1 if students else 1,
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(student)
    save_students(students)
    print("Student added successfully!")

@log_operation
def read_students():
    students = load_students()
    for student in students:
        yield student

@log_operation
def update_student(student_id, key, value):
    students = load_students()
    for student in students:
        if student["id"] == student_id:
            student[key] = value
            save_students(students)
            print("Student updated.")
            return
    print("Student not found!")

@log_operation
def delete_student(student_id):
    students = load_students()
    new_list = [s for s in students if s["id"] != student_id]
    save_students(new_list)
    print("Student deleted if existed.")

def sort_by_key(key):
    students = load_students()
    sorted_students = sorted(students, key=lambda x: x[key])
    for s in sorted_students:
        print(s)

def menu():
    while True:
        print("\n1. Add Student\n2. View All Students\n3. Update Student\n4. Delete Student\n5. Sort Students\n6. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            marks = float(input("Marks: "))
            create_student(name, age, marks)

        elif choice == "2":
            for stu in read_students():
                print(stu)

        elif choice == "3":
            sid = int(input("Student ID: "))
            key = input("Field to update (name/age/marks): ")
            value = input("New Value: ")
            if key == "age":
                value = int(value)
            elif key == "marks":
                value = float(value)
            update_student(sid, key, value)

        elif choice == "4":
            sid = int(input("Student ID to delete: "))
            delete_student(sid)

        elif choice == "5":
            key = input("Sort by (name/age/marks): ")
            sort_by_key(key)

        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
