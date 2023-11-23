# Packing and unpacking of dictionaries
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = person.items()
# print(a1, a2)
# print(b1, b2)

# for key, value in person.items():
# print(key, value)

person = {
    'name': 'Aline',
    'surname': 'Souza',
}

person_data = {
    'age': 16,
    'height': 1.6,
}

complete_people = {**person, **person_data}
# print(people_complete)

# args and kwargs
# args (already seen)
# kwargs - keyword arguments (named arguments)


def show_named_arguments(*args, **kwargs):
    print('UNNAMED:', args)

    for key, value in kwargs.items():
        print(key, value)


# show_named_arguments(name='Joana', qlq=123)
# show_named_arguments(**complete_people)

settings = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
show_named_arguments(**settings)