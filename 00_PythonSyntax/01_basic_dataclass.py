from dataclasses import dataclass, field

#my practice
@dataclass
class Developer:
    name: str
    experience: int
    tech_stack: list[str] =field(default_factory = list)   #default_factory is a function that returns a default value for the field
    based_in: str | None = None # defining optional field, input will be either a string or None


    #experimenting with using dataclass attribute in method 
    def is_senior(self) -> bool:
        return self.experience >= 3
    

dev1 = Developer(name = "Amraha", experience = 1, tech_stack = ["Typescript", "Nextjs"], based_in = "Pakistan")
dev2 = Developer(name = "Amr", experience = 2, tech_stack = ["Python", "Django"])  #optional field left empty
dev3 = Developer(name = "Amraha A.", experience = 4, based_in = "Tokyo")  #tech_stack is empty list because it is not provided

print(f"Developer1: {dev1}")
print(f"Developer2: {dev2}")
print(f"Developer3: {dev3}")

# Output ☝🏻
# Developer1: Developer(name='Amraha', experience=1, tech_stack=['Typescript', 'Nextjs'], based_in='Pakistan')
# Developer2: Developer(name='Amr', experience=2, tech_stack=['Python', 'Django'], based_in=None)
# Developer3: Developer(name='Amraha A.', experience=4, tech_stack=[], based_in='Tokyo')


print(f"Is {dev1.name} Senior?  {dev1.is_senior()}")
print(f"Is {dev2.name} Senior?  {dev2.is_senior()}")
print(f"Is {dev3.name} Senior?  {dev3.is_senior()}")

# Output ☝🏻
# Is Amraha Senior?  False
# Is Amr Senior?  False
# Is Amraha A. Senior?  True




