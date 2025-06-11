
from typing import TypeVar, Any

# --------------------WITHOUT GENERICS-----------------------


def first_element(item: list[Any]) -> Any:
    return item[0]

nums = [5, 10, 15, 20]
string = ["abc", "def"]

num_list = first_element(nums)
str_list = first_element(string)
print("\nWITHOUT GENERIC TYPING")
print(f"List of Numbers: {num_list}")
print(f"List of strings: {str_list}\n")


# --------------------WITH GENERIC Typing-----------------------

T = TypeVar("T")

def generic_first_element(item: list[T]) -> T:
    return item[0]


nums = [5, 10, 15, 20]
string = ["abc", "def", "ghi"]

list_of_nums = generic_first_element(nums) 
list_of_str = generic_first_element(string)

print("WITH GENERIC TYPING")
print(f"List of Numbers: {list_of_nums}")
print(f"List of Strings: {list_of_str}\n")

# OUTPUT 👇🏻
# WITHOUT GENERIC TYPING
# List of Numbers: 5
# List of strings: abc

# WITH GENERIC TYPING
# List of Numbers: 5
# List of Strings: abc


# IMPORTANT 📍
# Both versions return the same result at runtime no errors occur
# The key difference is that generic typing adds type safety and helps catch errors during development (with tools like mypy),
# while non-generic typing works but doesn’t preserve specific type info across function calls
# It ensures the input and output types stay consistent
