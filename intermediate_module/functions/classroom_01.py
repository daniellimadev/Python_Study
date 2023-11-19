"""
Introduction to functions (def) in Python
Functions are pieces of code used to
replicate a certain action throughout your code.
They can receive values ​​for parameters (arguments)
and return a specific value.
By default, Python functions return None.
"""


# def Print(a, b, c):
# print('Multiple1')
# print('Multiple2')
# print('Multiple3')
# print('Multiple4')

# def print(a, b, c):
# print(a, b, c)


# print(1, 2, 3)
# print(4, 5, 6)

def greeting(name='No name'):
    print(f'Hello, {name}!')


greeting('Daniel Pereira')
greeting('Maria')
greeting('Helena')
greeting()