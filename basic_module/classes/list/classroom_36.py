"""
Lists in Python
List type - Mutable
Supports multiple values ​​of any type
Reusable insights - indexes and slicing
Useful methods:
    append - Adds an item to the end
    insert - Adds an item to the chosen index
    pop - Remove from the end or chosen index
    del - delete an index
    clear - clears the list
    extend - extends the list
    + - concatenates lists
Create Read Update Delete
Create, read, change, delete = list[i] (CRUD)
"""
#0 1 2 3
list = [10, 20, 30, 40]
list.append('Luiz')
name = list.pop()
list.append(1233)
del list[-1]
# list.clear()
list.insert(100, 5)
print(list[4])