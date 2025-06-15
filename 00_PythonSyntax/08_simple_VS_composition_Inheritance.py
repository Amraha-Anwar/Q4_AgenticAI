from dataclasses import dataclass, field, fields
from typing import Optional

# ----------------------SIMPLE INHERITANCE---------------------------
@dataclass
class Person:
    name: str
    age: int

    def greet(self)->str :
        return f"Hello {self.name}! Hope you are doing well :)"
    
@dataclass
class InheritedEmployee(Person):         #inheritance
    employee_id : int
    department: str
    salary: float = 0.0
    email: Optional[str] = None
    skills: list[str] = field(default_factory=list)

    def work(self)-> str:
        return f"{self.name} works in {self.department} department."
    
    def add_skills(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)

def simple_inheritance():
    employee = InheritedEmployee(
        name="captian America",
        age= 45,
        employee_id= 34215,
        department= "IT",
        salary= 100000.00,
        email= "abc@gmail.com",
        skills=["Data Analysis", "debugging", "maintainance"]
    )
    print(f"Employee: {employee}")
    print(f"Employee Name: {employee.name}")
    print(f"Employee Age: {employee.age}")
    print(f"Employee email: {employee.email}")
    print(f"Employee's Skills: {employee.skills}")
    print(f"{employee.greet()}")
    print(f"{employee.work()}")

    employee.add_skills("Cyber Security")
    print(f"Employees's additional skills : {employee.skills}")

    # showing all fields
    all_fields = fields(Employee)
    print("\nAll fields in Employee class:")
    for f in all_fields:
        print(f"{f.name}: {f.type}")


# ----------------------COMPOSITION ALTERNATIVE---------------------------

@dataclass
class PersonInfo:
    name: str
    age: int
    email: Optional[str] = None

@dataclass
class Employee:
    person: PersonInfo
    employee_id : int
    department: str
    salary: float = 0.0
    skills: list[str] = field(default_factory=list)

    def greet(self) -> str:
        return f"Hello {self.person.name}! How have you been?"
    
    def work(self)-> str:
        return f"{self.person.name} works in {self.department} department."
    
    def add_skills(self, skill:str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)

def composition():
    person = PersonInfo(
        name= "Amraha A.",
        age= 34,
        email= "abc@gmail.com"
    )

    employee = Employee(
        person = person,
        employee_id = 31342,
        department = "Managing",
        salary = 85000.00,
        skills = ["Machine Learning", "Data Structure"]
    )
    print(f"Employee : {employee}")
    print(f"Employee's name via person: {employee.person.name}") #person's attributes through the composition
    print(f"Employee's age via person: {employee.person.age}")
    print(f"Person's email: {employee.person.email}") 
    print(f"Employee's Skills: {employee.skills}")
    print(f"Greeting: {employee.greet()}")
    print(f"Working: {employee.work()}")



if __name__ == "__main__":
    print("\n\t\t====SIMPLE INHERITANCE====\n")
    simple_inheritance()
    print("\n\t\t====COMPOSITION ALTERNATIVE====\n")
    composition() 



# OUTPUT 👇🏻
#      ====SIMPLE INHERITANCE====

# Employee: InheritedEmployee(name='captian America', age=45, employee_id=34215, department='IT', salary=100000.0, email='abc@gmail.com', skills=['Data Analysis', 'debugging', 'maintainance'])
# Employee Name: captian America
# Employee Age: 45
# Employee email: abc@gmail.com
# Employee's Skills: ['Data Analysis', 'debugging', 'maintainance']
# Hello captian America! Hope you are doing well :)
# captian America works in IT department.
# Employees's additional skills : ['Data Analysis', 'debugging', 'maintainance', 'Cyber Security']

# All fields in Employee class:
# person: <class '__main__.PersonInfo'>
# employee_id: <class 'int'>
# department: <class 'str'>
# salary: <class 'float'>
# skills: list[str]

#                 === COMPOSITION ALTERNATIVE ===
# Employee : Employee(person=PersonInfo(name='Amraha A.', age=34, email='abc@gmail.com'), employee_id=31342, department='Managing', salary=85000.0, skills=['Machine Learning', 'Data Structure'])
# Employee's name via person: Amraha A.
# Employee's age via person: 34
# Person's email: abc@gmail.com
# Employee's Skills: ['Machine Learning', 'Data Structure']
# Greeting: Hello Amraha A.! How have you been?
# Working: Amraha A. works in Managing department.