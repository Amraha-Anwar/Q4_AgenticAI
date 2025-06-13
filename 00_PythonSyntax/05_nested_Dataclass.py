from dataclasses import dataclass, field, asdict
from typing import Optional
import json

@dataclass
class Address:
    street: str
    city: str
    state: str
    country: str = "USA"

@dataclass
class Grade:
    class_grade : str
    section : Optional[str] = None


@dataclass
class Student:
    name : str
    fatherName : str
    age : int
    address : Address
    grade : Grade
    roll_no : int
    subjects : list[str] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)
    
    def add_subject(self, subject: str) -> None:
        if subject not in self.subjects:
            self.subjects.append(subject)


def run():
    address = Address(
        street = "abc street",
        city = "Los Angeles",
        state = "AZ",
    )

    grade = Grade(
        class_grade = "8th",
        section = "Lilly",
    )

    student = Student(
        name = "Amr..",
        fatherName= "an..",
        age = 43,
        address = address,
        grade = grade,
        roll_no = 3073,
        subjects = ["Computer Science", "Physics"],
    )

    print(f"Student: {student.name}")
    print(f"Grade: {grade.class_grade}")
    print(f"Roll NO: {student.roll_no}")
    print(f"Subjects: {student.subjects}")
    

    student.add_subject("Chemistry")
    print(f"Updated Subjects List: {student.subjects}")

    print("\nStudent JSON: ")
    print(student.to_json())

if __name__ == "__main__":
    print("=== NESTED DATACLASS EXAMPLE ===")
    run()


# OUTPUT 👇🏻
# === NESTED DATACLASS EXAMPLE ===
# Student: Amr..
# Grade: 8th
# Roll NO: 3073
# Subjects: ['Computer Science', 'Physics']
# Updated Subjects List: ['Computer Science', 'Physics', 'Chemistry']

# Student JSON: 
# {
#   "name": "Amr..",
#   "fatherName": "an..",
#   "age": 43,
#   "address": {
#     "street": "abc street",
#     "city": "Los Angeles",
#     "state": "AZ",
#     "country": "USA"
#   },
#   "grade": {
#     "class_grade": "8th",
#     "section": "Lilly"
#   },
#   "roll_no": 3073,
#   "subjects": [
#     "Computer Science",
#     "Physics",
#     "Chemistry"
#   ]
# }