"""
enumerate - enumerates iterables (indices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
list = ['Maria', 'Helena', 'Daniel']
list.append('John')

for index, name in enumerate(list):
    print(index, name, list[index])

# for item in enumerate(list):
# index, name = item
# print(index, name)


# for enumerated_tuple in enumerate(list):
# print('FOR of tuple:')
# for value in enumerated_tuple:
# print(f'\t{value}')