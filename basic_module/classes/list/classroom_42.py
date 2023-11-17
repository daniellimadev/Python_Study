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
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
list_a.extend(list_b)
print(list_a)