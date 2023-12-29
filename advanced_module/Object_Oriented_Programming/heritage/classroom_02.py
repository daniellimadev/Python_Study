# super() and member overlap - Object-Oriented Python
# Main class (Person)
# -> super class, base class, parent class
# Child classes (Client)
# -> sub class, child class, derived class
# class MyString(str):
# def upper(self):
# print('CALLED UPPER')
# return = super(MyString, self).upper()
# print('AFTER UPPER')
# return return


# string = MinhaString('Luiz')
# print(string.upper())

class A(object):
    attribute_a = 'value a'

    def __init__(self, attribute):
        self.attribute = attribute

    def method(self):
        print('A')


class B(A):
    attribute_b = 'value b'

    def __init__(self, attribute, other_thing):
        super().__init__(attribute)
        self.other_thing = other_thing

    def method(self):
        print('B')


class C(B):
    attribute_c = 'value c'

    def __init__(self, *args, **kwargs):
        # print('HEY, I cheated the system.')
        super().__init__(*args, **kwargs)

    def method(self):
        # super().method() # B
        # super(B, self).method() # A
        # super(A, self).method() # object
        A.method(self)
        B.method(self)
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Attribute', 'Any')
# print(c.attribute)
# print(c.outra_coisa)
c.method()
# print(c.attributo_a)
# print(c.attributo_b)
# print(c.attributo_c)
# c.method()