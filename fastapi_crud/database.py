import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "students.json")

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        json.dump([], f)

def load_students():
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_students(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
