"""
Higher Order Functions
First-class functions
"""


def greeting(msg, name):
    return f'{msg}, {name}!'


def execute(function, *args):
    return function(*args)


print(
    execute(greeting, 'Good morning', 'Daniel')
)
print(
    execute(greeting, 'Good evening', 'Maria')
)
