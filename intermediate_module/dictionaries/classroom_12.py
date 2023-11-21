# Useful dictionary methods in Python
# len - how many keys
# keys - iterable with keys
# values ​​- iterable with values
# items - iterable with keys and values
# setdefault - adds value if key does not exist
# copy - returns a shallow copy (shallow copy)
# get - get a key
# pop - Deletes an item with the specified key (del)
# popitem - Deletes the last added item
# update - Updates one dictionary with another
person = {
    'name': 'Luiz Otávio',
    'surname': 'Miranda',
    'age': 900,
}

person.setdefault('age', 0)
print(person['age'])
# print(len(person))
# print(list(person.keys()))
# print(list(person.values()))
# print(list(person.items()))

# for value in person.values():
# print(value)

# for key, value in person.items():
# print(key, value)