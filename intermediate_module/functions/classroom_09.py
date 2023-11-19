"""
Closure functions that return other functions!!
"""

def create_greeting(salutation, name):
    def greet():
        return f'{salutation}, {name}'
    return greet

create1 = create_greeting('Good morning', 'Daniel')
create2 = create_greeting('Goodnight', 'Daniel')

print(create1())
print(create2())