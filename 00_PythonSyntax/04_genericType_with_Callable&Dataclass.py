from dataclasses import dataclass
from typing import TypeVar, Generic, Callable

T = TypeVar("T")                      # Generic type variable

@dataclass
class Processor(Generic[T]):          # Generic class (works with data of type T)
    value: T                          # Type hinting for the value
    func: Callable[[T], T]            # Takes a value of type T and returns a value of type T

    def process(self) -> T:
        return self.func(self.value)

def double(x: int) -> int:            # Function to be passed to 'func' defined above
    return x * 2

p = Processor(func=double, value=10)
print(p.process())
