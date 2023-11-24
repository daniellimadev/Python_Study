"""
Considering two lists of integers or floats (list A and list B)
Add the values ​​in the lists, returning a new list with the added values:
If one list is larger than the other, the sum will only take into account the size of the list.
smaller.
Example:
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]
=================== result
sum_list = [2, 4, 6, 8]
"""
list_a = [10, 2, 3, 40, 5, 6, 7]
list_b = [1, 2, 3, 4]
sum_list = [x + y for x, y in zip(list_a, list_b)]
print(sum_list)

# sum_list = []
# for i in range(len(lista_b)):
# list_sum.append(list_a[i] + list_b[i])
# print(sum_list)

# sum_list = []
# for i, _ in enumerate(lista_b):
# list_sum.append(list_a[i] + list_b[i])
# print(sum_list)