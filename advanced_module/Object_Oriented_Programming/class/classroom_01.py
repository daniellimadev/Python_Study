# Class are templates for creating new objects
# class generate new objects (instances) that
# can have their own attributes and methods.
# Objects generated by the class can use its data
# internals to perform various actions.
# By convention, we use PascalCase for file names
# class.
# string = 'Daniel' # str
# print(string.upper())
# print(isinstance(string, str))
class Person:
    ...


p1 = Person()
p1.name = 'Daniel'
p1.surname = 'Pereira'

p2 = Person()
p2.name = 'Maria'
p2.surname = 'Joana'

print(p1.name)
print(p1.surname)

print(p2.name)
print(p2.surname)