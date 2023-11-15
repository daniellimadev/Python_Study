"""
Lists in Python
List type - Mutable
Supports multiple values of any type
Reusable insights - indexes and slicing
Useful methods:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Create, read, change, delete = list[i] (CRUD)
"""
#0 1 2 3 4 5
list = [10, 20, 30, 40]
# list[2] = 300
# from list[2]
# print(list)
# print(list[2])
list.append(50)
list.pop()
list.append(60)
list.append(70)
last_value = list.pop(3)
print(list, 'Removed,', last_value)