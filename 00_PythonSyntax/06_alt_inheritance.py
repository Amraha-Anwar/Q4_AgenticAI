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

# --------------------------------------------------------------------------------------------------------------------
# COMPOSITION PATTERN

@dataclass
class PersonInfo:
    name : str
    birth_date : date
    email: Optional[str] = None

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month , self.birth_date.day)
        )
    
@dataclass
class TeachingStaff:           
    person : PersonInfo       # Composition instead of Inheritance
    employee_id : str
    department : str
    courses_taught : list[str] = field(default_factory = list)
    salary : float = 0.0

    @property
    def name(self) -> str:
        return self.person.name
    
    @property
    def age(self) -> int:
        return self.person.age
    
    @property
    def email(self) -> Optional[str]:
        return self.person.email
    
    def add_course(self, course: str) -> str:
        if course not in self.courses_taught:
            return self.courses_taught.append(course)
        
def demo_composition():
    person_info = PersonInfo(
        name="Dr. Jane Smith",
        birth_date=date(1980, 3, 15),
        email="jane.smith@university.edu"
    )
    
    # teaching staff with person info
    instructor = TeachingStaff(
        person=person_info,
        employee_id="E54321",
        department="Mathematics",
        courses_taught=["Calculus", "Linear Algebra"],
        salary=78000.0,
    )
    
    print("\n=== APPROACH 2: COMPOSITION ===")
    print(f"Instructor: {instructor.name}, Age: {instructor.age}")
    print(f"Department: {instructor.department}")
    print(f"Email: {instructor.email}")
    instructor.add_course("Statistics")
    print(f"Courses taught: {instructor.courses_taught}")

# -----------------------------------------------------------------------------------------------------------------
# COMPOSITION WITH DELEGATION


@dataclass
class BaseWithDefaults:
    name: str
    description: Optional[str] = None


@dataclass
class CompositionBased:
    base: BaseWithDefaults
    required_id: str
    optional_value: int = 0
    

    @property
    def name(self) -> str:
        return self.base.name
    
    @property
    def description(self) -> Optional[str]:
        return self.base.description
    
    def __post_init__(self):
        if not self.required_id.strip():
            raise ValueError("required_id cannot be empty")


def demo_composition_delegation():
    try:
        base = BaseWithDefaults(
            name="Test Name",
            description="Optional description"
        )
        
        valid = CompositionBased(
            base=base,
            required_id="12345"
        )
        
        print("\n=== APPROACH 3: COMPOSITION WITH DELEGATION ===")
        print(f"Composed object: {valid}")
        print(f"Accessing delegated properties - Name: {valid.name}, Description: {valid.description}")
        

        invalid = CompositionBased(
            base=BaseWithDefaults(name="Invalid"),
            required_id="",  
        )
        print(f"Invalid instance: {invalid}")  
    except ValueError as e:
        print(f"Validation error: {e}")

if __name__ == "__main__":
    demo_no_inheritance()
    demo_composition()
    demo_composition_delegation() 




# OUTPUT 👇🏻
# === APPROACH 1: STANDALONE CLASSES ===
# Student: Alice Johnson, Age: 25, Major: Computer Science
# Date of Birth: 2000-05-15
# Student courses: ['Python Programming', 'Data Structures', 'Algorithms']
# Is honors student? True

# === APPROACH 2: COMPOSITION ===
# Instructor: Dr. Jane Smith, Age: 45
# Department: Mathematics
# Email: jane.smith@university.edu
# Courses taught: ['Calculus', 'Linear Algebra', 'Statistics']

# === APPROACH 3: COMPOSITION WITH DELEGATION ===
# Composed object: CompositionBased(base=BaseWithDefaults(name='Test Name', description='Optional description'), required_id='12345', optional_value=0)
# Accessing delegated properties - Name: Test Name, Description: Optional description
# Validation error: required_id cannot be empty