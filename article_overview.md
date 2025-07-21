
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

### What Is Decorators?
A decorator is a function in python that allows us to add extra functionality like logging, access control to another function without changing its original code. We can you this “@” symbol to apply a decorator to a function.

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

### What Is Generators?
- A generator is a function in python that returns value one by one using the “yield” keyword instead of return.
- Yield is pause and resume the activity
- It doesn’t store all values in memory so its memory efficient and useful for large data.


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

### What Is Lambda?
A lambda is an anonymous function in python used to write small, one-line functions without defining them using def. It can take any number of arguments but can have only one expression.

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
- **List**:
``` 
A list in Python is an ordered collection used to store multiple items in a single variable. It is written using square brackets [] and can hold elements of any data type.
```
- **Dict**: 
```
A dictionary in Python is a collection of key-value pairs. It is unordered mutable, and does not allow duplicate keys. It is defined using curly braces {} with keys and values separated by a colon.
```

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

## Section-Wise Interview Questions
### 1. Decorators
```
- What is a decorator in Python? How does it work?

- How are decorators useful in API development?

- Can you write a decorator that checks if a user is logged in?

- What are the drawbacks of using multiple decorators on a single function?

- What is the difference between function decorators and class decorators?
```


### 2. Generators
```
- What is the difference between a generator and a normal function?

- Why are generators memory-efficient?

- Can you give a use case where a generator would be better than a list?

- What happens if you try to iterate over a generator twice?

- Explain the difference between yield and return.
```

### 3. Lambda Functions
```
- What are lambda functions? When would you use one?

- How is lambda different from a regular function (def)?

- Can you give examples of using lambda with map(), filter(), and sorted()?

- Why are lambda functions limited in their scope (e.g., no assignment statements)?

- Are lambda functions object-oriented or functional in nature?
```

### 4. Dictionaries & Lists
```
- What’s the time complexity of searching in a list vs a dictionary?

- How do you handle duplicates in a list of dictionaries?

- How do you sort a list of dictionaries by a key (e.g., student name)?

- What are the methods used to manipulate lists and dictionaries?

- How do you merge two dictionaries in Python 3.9+?
```

### 5. CRUD Operations in CLI/API
```
- What is CRUD and why is it important?

- How would you implement CRUD using a list of dictionaries?

- How is the POST method different from PUT in FastAPI?

- How do you handle data validation in FastAPI?

- How would you test your FastAPI endpoints using Postman?
```

### 6. FastAPI Specific
```
- What are the benefits of FastAPI over Flask or Django?

- How does FastAPI handle type validation?

- How do you write custom exception handlers in FastAPI?

- What is the role of Pydantic models in FastAPI?

- How do you use dependency injection in FastAPI?
```
