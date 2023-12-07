# Methods in Python class instances
# Hard coded - It is something that was written directly in the code
class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} is accelerating...')


string = 'Daniel'
print(string.upper())

beetle = Car('Beetle')
print(beetle.name)
beetle.accelerate()

velar = Car(name='velar')
print(velar.name)
velar.accelerate()