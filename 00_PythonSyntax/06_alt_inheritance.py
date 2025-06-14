from dataclasses import dataclass, field
from typing import Optional
from datetime import date


#  STANDALONE APPROACH
@dataclass
class Person:
    name : str
    birth_date : date

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

@dataclass
class PersonWithEmail(Person):
    email : Optional[str] = None


@dataclass
class Student:
    name : str
    birth_date : date
    student_id : int
    major : str
    email : Optional[str] = None
    gpa : float = 0.0
    courses : list[str] = field(default_factory = list)

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
    
    def add_course(self, course : str) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def is_honors(self) -> bool:
        return self.gpa > 3.5
    

def demo_no_inheritance():
    """Demonstrate the standalone approach."""
    student = Student(
        name="Alice Johnson",
        birth_date=date(2000, 5, 15),
        student_id="S12345",
        major="Computer Science",
        email="alice@university.edu",
        gpa=3.8,
        courses=["Python Programming", "Data Structures"]
    )
    
    print("=== APPROACH 1: STANDALONE CLASSES ===")
    print(f"Student: {student.name}, Age: {student.age}, Major: {student.major}")
    print(f"Date of Birth: {student.birth_date}")
    student.add_course("Algorithms")
    print(f"Student courses: {student.courses}")
    print(f"Is honors student? {student.is_honors()}")

if __name__ == "__main__":
    demo_no_inheritance()

