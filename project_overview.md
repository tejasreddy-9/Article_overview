# Decorators, Generators, Lambda, Dict, List - CRUD Console App and API
# Student Management System - Console + API (CRUD)

## Project Overview

- This project is a Student Management System with both Console and API interfaces.
- It performs CRUD operations using Python features like Decorators, Generators, Lambda, Dict, and List.
- The system is lightweight, easy to use.


## Client Requirements

- Store and manage student records
- Console-based CLI interface for CRUD
- FastAPI for remote access
- Use Python core: Decorators, Generators, Lambda, Dict, List

---

## Core Technologies Used

- **Language**: Python
- **Web Framework**: FastAPI
- **Data Structure**: List + Dict
- **Other Concepts**:
  - Decorators (logging & auth)
  - Generators (streaming student list)
  - Lambda (sorting/filtering)
- **Execution**: Postman for API

---


## Decorators:
A decorator is a function in python that allows us to add extra functionality like logging, access control to another function without changing its original code. We can you this “@” symbol to apply a decorator to a function.
Example:
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
@log
def create():
    print("Student created")
create()

---

## Generators:
A generator is a function in python that returns value one by one using the “yield” keyword instead of return.
Yield is pause and resume the activity
It doesn’t store all values in memory so its memory efficient and useful for large data.
Example:
students = [{"id": 1, "name": "Tejas"}]
def get_students():
    for student in students:
        yield student
for s in get_students():
    print(s)

---

## Lambda:
A lambda is an anonymous function in python used to write small, one-line functions without defining them using def. It can take any number of arguments but can have only one expression.
Example:
students = [{"id": 1, "name": "Tejas"}, {"id": 2, "name": "Rahul"}]
search = list(filter(lambda s: "tejas" in s["name"].lower(), students))
print(search)

---

## Dict (Dictionary):
A dictionary in Python is a collection of key-value pairs. It is unordered mutable, and does not allow duplicate keys. It is defined using curly braces {} with keys and values separated by a colon.
Example:
students = [] 
def add_student(s_id, name):
    students.append({"id": s_id, "name": name})
add_student(1, "Tejas")
print(students)

---

## CRUD
Create, Read, Update, Delete.

Create:
Used to add new data into the database.

Read:
Used to fetch data from the database

Update:
Used to modify or change existing data in the database.

Delete:
Used to remove data from the database.

---

### 1. Requirement Gathering
- Understand user roles & operations
- Console and API support
- Simple, in-memory system

### 2. System Design
- In-memory Dict/List
- Modular code structure
- Separate logic for console & API

### 3. Implementation
- CLI: main_console.py
- API: main_api.py
- Shared utilities and models

### 4. Testing
- Postman tests for API
- Handle invalid inputs

### 5. Deployment
- Console: Python run
- API: `uvicorn main_api:app --reload`

---

## Process Flow

```
flowchart TD
  1. Start
  2. User chooses Console Mode or API Mode
  3. If Console Mode selected:
    -  Display the CRUD operation menu
    -  Perform CRUD on student records using Dict and List
  4. If API Mode selected:
    -  User sends API request via Postman or Swagger
    -  FastAPI handles the CRUD route
  5. Data is saved or updated in the in-memory structure
  6. Response is returned in JSON format (for API) or printed (for Console)
  7. End
```

---

## Structure

```
student_crud_project/
│
├── main.py              # FastAPI app
├── models.py            # Pydantic schemas
├── database.py          # In-memory student DB
├── utils.py             # Generators, Lambda, Decorators
├── logger.py            # Logging decorator
├── requirements.txt     # FastAPI, Uvicorn, etc.
└── project_overview.md  # Documentation
```

---

