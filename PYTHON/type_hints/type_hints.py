######### without type_hints #######

def add(a,b):
 print(a+b)

add(2,2)

######### with type_hints ###########

def mul(a:int,b:int)->int:
 print(a+b)

mul(2,2)
mul("ganesh","dinesh")

#################### list[t] #######################
def calculate_total(marks: list[int]) -> int:
    return sum(marks)


print(calculate_total([80, 90, 75]))


###################### dict[K, V] #########################

students: dict[str, int] = {
    "Arun": 85,
    "Bala": 90,
    "Ravi": 78,
}

print(students["Bala"])


########################### type_hints ############################

# this allows the return value will be the mentioned type or None

from typing import Optional


def get_email(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "arun@example.com"

    return None


print(get_email(1))
print(get_email(2))


############################## Union ##################################

# this allows the parmas should be any of the data types mentioned

from typing import Union


def display_id(user_id: Union[int, str]) -> None:
    print(user_id)


display_id(101)
display_id("USER101")


############################### Any ##################################
from typing import Any


def display(value: Any) -> None:
    print(value)


display(10)
display("Hello")
display([1, 2, 3])


################# callable #######################################

from collections.abc import Callable


def calculate(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


print(calculate(5, 3, add))
print(calculate(5, 3, multiply))

# Callable[[int, int], int]
# #         ^^^^^^^^^  ^^^
# #         inputs     return type





