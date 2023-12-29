# Simple inheritance - Relations between classes
# Association - uses, Aggregation - has
# Composition - Owns, Inheritance - Is a
#
# Inheritance vs Composition
#
# Main class (Person)
# -> super class, base class, parent class
# Child classes (Client)
# -> sub class, child class, derived class
class Person:
    cpf = '1234'

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def speak_class_name(self):
        print('Class PERSON')
        print(self.name, self.surname, self.__class__.__name__)


class Person(Person):
    def speak_class_name(self):
        print("YEAH, I didn't even leave the CLIENT class")
        print(self.name, self.surname, self.__class__.__name__)


class Student(Person):
    cpf = 'student cpf'
    ...


c1 = Person('Luiz', 'Otávio')
c1.speak_class_name()
a1 = Student('Maria', 'Helena')
a1.speak_class_name()
print(a1.cpf)
# help(Client)