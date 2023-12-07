# Scope of the class and class methods
class Animal:
    # name = 'Lion'

    def __init__(self, name):
        self.name = name

        variable = 'value'
        print(variable)

    def eating(self, food):
        return f'{self.name} is command {food}'

    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)


lion = Animal(name='Lion')
print(lion.name)
print(lion.execute('apple'))