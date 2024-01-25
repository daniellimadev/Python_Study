# dataclasses - What are dataclasses?
# The dataclasses module provides a decorator and functions to create methods like
# __init__(), __repr__(), __eq__() (among others) in classes defined by the
# user.
# In summary: dataclasses are syntax sugar for creating normal classes.
# It was described in PEP 557 and added in Python 3.7.
#doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


if __name__ == '__main__':
    p1 = Person('Luiz', 30)
    p2 = Person('Luiz', 30)
    print(p1 == p2)