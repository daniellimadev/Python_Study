import sys

# Generator expression, Iterables and Iterators in Python
iterable = ['I', 'Have', '__iter__']
iterator = iter(iterable) # has __iter__ and __next__
list = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(list))
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
# print(n)