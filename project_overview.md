
# Masterclass: Understand Decorators, Generators, Lambda, Dict, List – CRUD Console App and API

## Overview

This masterclass strengthens your foundation in Python’s key features—Decorators, Generators, Lambda functions, Dictionary, and List—by applying them to real-world use cases such as using Console (CLI) and FastAPI-based API. You’ll understand the what, why, and how of each concept and apply them in a modular, scalable CRUD architecture.


## Core Technologies Used

- **Language**: Python
- **Web Framework**: FastAPI
- **Data Structure**: List + Dict
- **Other Concepts**:
  - Decorators (logging & auth)
  - Generators (streaming student list)
  - Lambda (sorting/filtering)
- **Execution**: Postman for API

## Section 1: Decorators

### What Is It?
Decorators wrap around a function to add extra behavior without modifying the function's code.

### Where to Use
- Logging
- Validation
- Authentication
- Access control

### Drawbacks
- May make debugging harder if overused.
- Can become complex when stacking multiple decorators.

### Example
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def create():
    print("Student created")
```

## Section 2: Generators

### What Is It?
Generators use `yield` to return items one at a time, ideal for large datasets or streaming.

### Where to Use
- Reading large files
- Streaming DB results
- Real-time pagination

### Drawbacks
- One-time use (cannot rewind)
- Slightly more complex syntax

### Example
```python
students = [{"id": 1, "name": "Tejas"}]

def get_students():
    for student in students:
        yield student

for s in get_students():
    print(s)
```

## Section 3: Lambda Functions

### What Is It?
One-liner anonymous functions for small operations, often used with `map`, `filter`, `sorted`.

### Where to Use
- Sorting/filtering on-the-fly
- Short callbacks
- Quick logic inside loops

### Drawbacks
- Poor readability for complex operations
- Can’t include multiple statements

### Example
```python
students = [{"id": 1, "name": "Tejas"}, {"id": 2, "name": "Rahul"}]
search = list(filter(lambda s: "tejas" in s["name"].lower(), students))
```

## Section 4: Dictionaries and Lists

### What Are They?
- **List**: Ordered collection, used for student record list.
- **Dict**: Key-value structure, used per student.

### Where to Use
- In-memory DB simulations
- Rapid prototyping
- Data lookups and transformations

### Drawbacks
- No persistence (non-permanent storage)
- Can’t handle large-scale DB use-cases

### Example
```python
students = []

def add_student(s_id, name):
    students.append({"id": s_id, "name": name})
```

## Section 5: CRUD Operations

### What is CRUD?
Create, Read, Update, Delete.

***Create***:
Used to add new data into the database.

***Read***:
Used to fetch data from the database

***Update***:
Used to modify or change existing data in the database.

***Delete***:
Used to remove data from the database.

## Development Phases

1. **Requirement Gathering**
   - CLI and API need
   - User roles: admin, guest

2. **System Design**
   - List + Dict for DB
   - Decorator: `@log_action`
   - Generator: `yield student`
   - Lambda: sorting, filtering

3. **Implementation**
   - `main_console.py`: CLI
   - `main_api.py`: FastAPI
   - `utils.py`: Common logic

4. **Testing**
   - Console inputs
   - API testing via Postman

5. **Deployment**
   - Console: Run with Python
   - API: `uvicorn main_api:app --reload`

## Process Flow Diagram

```mermaid
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

## Structure

```
student_crud_project/
├── main.py              # FastAPI main app
├── main_console.py      # Console CLI interface
├── models.py            # Pydantic models
├── database.py          # In-memory list/dict DB
├── utils.py             # Decorators, Lambda, Generator
├── logger.py            # Logging decorators
├── requirements.txt     # FastAPI, Uvicorn
└── project_overview.md  # Full documentation
```

## Conclusion

By mastering these core Python tools and concepts within a practical CRUD system, you'll gain not just theoretical knowledge but also real-world coding skills. The combination of Console App and FastAPI gives you both local and remote interfaces for learning development end-to-end.
