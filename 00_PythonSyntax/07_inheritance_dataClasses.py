from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Person:
    name: str
    age: int
    email_address: Optional[str] = None

@dataclass
class Teacher:
    name: str
    age: int
    email_address : Optional[str] = None
    subjects: list[str] = field(default_factory= list)

    def add_subjects(self, subject) -> str:
        if subject not in self.subjects:
            self.subjects.append(subject)

def main():
    print("\n\t\t\tPERSON")
    try:
        person = Person(
            name= "Amraha",
            age= 13,    
            # skipping email just to show it won't effect the result cuz it is set as optional
        )
        print(f"PERSON INFO: {person}")
    except Exception as e:
        print(f"Error Printing Person's Info :( {e}")

    print("\n\t\t\tTEACHER")
    try:
        teacher = Teacher(
            name= "Amraha A.",
            age = 34,
            email_address= "amraha123@gmail.com",
            subjects=["Mathematics", "Physics", "English"]
        )
        print(f"TEACHER INFO: {teacher}")
        teacher.add_subjects("Computer Science")
        print(f"UPDATED SUBJECTS LIST: {teacher.subjects}")
    except Exception as e:
        print(f"Error Printing Teacher's Info :( {e}")

if __name__ == "__main__":
    main()
    print(f"Program Completed Successfully! ")