# __dict__ and vars for instance attributes
class Person:
    current_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.current_year - self.age


data = {'name': 'John', 'age': 35}
p1 = Person(**data)
# p1.name = 'EITA'
# print(p1.age)
# p1.__dict__['other'] = 'thing'
# p1.__dict__['name'] = 'EITA'
# del p1.__dict__['name']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.other)
# print(p1.name)
print(vars(p1))
print(p1.name)