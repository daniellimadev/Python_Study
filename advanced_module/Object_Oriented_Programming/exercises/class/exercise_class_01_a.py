
# Exercise - Save your class in JSON
# Save your class data in JSON
# and then create the instances again
# of the class with the saved data
# Do it in separate files.

import json

FILE_PATH = 'exercise_class_01.json'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('John', 33)
p2 = Person('Helena', 21)
p3 = Person('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def make_dump():
    with open(FILE_PATH, 'w') as file:
        print('MAKING DUMP')
        json.dump(bd, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('HE IS THE __main__')
    make_dump()