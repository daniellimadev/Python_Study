"""
Exercise
Display list indexes
0 Maria
1 Helena
2 Luiz
"""
list = ['Maria', 'aline', 'Daniel']
list.append('John')


indices = range(len(list))

for index in indices:
    print(index, list[index], type(list[index]))