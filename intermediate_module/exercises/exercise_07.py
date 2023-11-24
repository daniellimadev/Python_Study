# Exercise - Join lists
# Create a zipper function (like clothes zipper)
# The job of this function will be to join two
# lists in order.
# Use all values ​​from the smallest list.
# E.g.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Result
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(l1, l2):
# interval = min(len(l1), len(l2))
# return [(l1[i], l2[i]) for i in range(interval)]
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='NO CITY')))