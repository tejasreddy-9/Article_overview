from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    marks: float

class StudentIn(BaseModel):
    name: str
    age: int
    marks: float
