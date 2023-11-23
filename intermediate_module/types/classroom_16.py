# Creating a set
# set(iterable) or {1, 2, 3}
# s1 = set('Daniel')
# s1 = set() # empty
# s1 = {'Daniel', 1, 2, 3} # with data
# Sets are efficient for removing duplicate values
# of iterables.
# - Your values ​​will always be unique;
# - Do not accept mutable values;
# - has no indexes;
# - do not guarantee order;
# - are iterable (for, in, not in)
#l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
#s1 = {1, 2, 3}
# print(3 not in s1)
# for number in s1:
# print(number)

# Useful methods:
# add, update, clear, discard
s1 = set()
s1.add('Daniel')
s1.add(1)
s1.update(('Hello world', 1, 2, 3, 4))
# s1.clear()
s1.discard('Hello world')
s1.discard('Daniel')
print(s1)

# Useful operators:
# union | union (union) - Unites
# intersection & (intersection) - Items present in both
# difference - Items present only in the set on the left
# symmetric difference ^ - Items that are not in both

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)