from dataclasses import dataclass, field

# --------------------WITH DATACLASS-------------------

@dataclass
class Developer:
    name: str
    experience: int
    tech_stack: list[str] =field(default_factory = list)  
    based_in: str | None = None 


    def is_senior(self) -> bool:
        return self.experience >= 3
    

dev1 = Developer(name = "Amraha", experience = 1, tech_stack = ["Typescript", "Nextjs"], based_in = "Pakistan")
dev2 = Developer(name = "Amr", experience = 2, tech_stack = ["Python", "Django"])  #optional field left empty
dev3 = Developer(name = "Amraha A.", experience = 4, based_in = "Tokyo")  #tech_stack is empty list because it is not provided

print("\n\t\t\t\tWITH DATACLASS\n")
print(f"Developer1: {dev1}")
print(f"Developer2: {dev2}")
print(f"Developer3: {dev3}\n")

# Output ☝🏻
# Developer1: Developer(name='Amraha', experience=1, tech_stack=['Typescript', 'Nextjs'], based_in='Pakistan')
# Developer2: Developer(name='Amr', experience=2, tech_stack=['Python', 'Django'], based_in=None)
# Developer3: Developer(name='Amraha A.', experience=4, tech_stack=[], based_in='Tokyo')


print(f"Is {dev1.name} Senior?  {dev1.is_senior()}")
print(f"Is {dev2.name} Senior?  {dev2.is_senior()}")
print(f"Is {dev3.name} Senior?  {dev3.is_senior()}\n")

# Output ☝🏻
# Is Amraha Senior?  False
# Is Amr Senior?  False
# Is Amraha A. Senior?  True


# --------------------WITHOUT DATACLASS-------------------

class Developer:
    def __init__(self, name, experience, based_in = None, tech_stack= None):  #complexity, have to write everything manually
        self.name = name
        self.experience = experience
        self.based_in = based_in
        # complexity, difficult to understand 👇🏻
        self.tech_stack = tech_stack if tech_stack is not None else []

    # manual string representation
    def __repr__(self) -> str:
        return f"Developer: {self.name}, experience: {self.experience}, based in: {self.based_in}, teck stack: {self.tech_stack}"
    
dev1 = Developer("Amraha", 1, "Pakistan", ["Typescript", "Nextjs"])
dev2 = Developer("Amraha A.", 4, "Tokyo")
dev3 = Developer("Amr", 0, ["Python"])

print("\t\t\t\tWITHOUT DATACLASS\n")
print(f"Developer1: {dev1}")
print(f"Developer2: {dev2}")
print(f"Developer3: {dev3}")




