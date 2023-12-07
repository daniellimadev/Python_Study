# Understanding "self" in Python class
# Class - Mold (usually no data)
# Instance of the class (object) - Has the data
# A class can generate multiple instances.
# In the class, self is the instance itself.
class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} is accelerating...')


beetle = Car('Beetle')
beetle.accelerate()
Car.accelerate(beetle)
# print(beetle.name)
# beetle.accelerate()

velar = Car(name='velar')
velar.accelerate()
Car.accelerate(velar)
# print(celtic.name)