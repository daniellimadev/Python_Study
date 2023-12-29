# Multiple Inheritance - Object-Oriented Python
# This means that in Python, a class can extend
# several other classes.
# Simple inheritance:
# Animal -> Mammal -> Human -> Person -> Client
# Multiple inheritance and mixins
# Log -> FileLog
# Animal -> Mammal -> Human -> Person -> Client
# Client(Person, FileLog)
#
# A B C D
# D(B, C) - C(A) - B(A) - A
#
# method -> speak
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 uses C3 superclass linearization
# to generate the mro.
# You don't need to study this (it's complex)
# https://en.wikipedia.org/wiki/C3_linearization
#
# To know the order in which methods are called
# Use the Class.mro() class method
# Or the __mro__ attribute (Dunder - Double Underscore)
class A:
    ...

    def who_am(self):
        print('A')


class B(A):
    ...

    # def who_am(self):
    # print('B')


class C(A):
    ...

    def who_am(self):
        print('C')


class D(B, C):
    ...

    def who_am(self):
        print('D')


d = D()
d.who_am()
# print(D.__mro__)
print(D.mro())