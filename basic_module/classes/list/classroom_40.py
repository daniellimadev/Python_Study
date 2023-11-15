"""
Exercise
Display list indexes
0 Maria
1 Helena
2 Luiz
"""
list = ['Maria', 'Helena', 'Luiz']
list.append('John')


indices = range(len(list))

for index in indices:
    print(index, list[index], type(list[index]))