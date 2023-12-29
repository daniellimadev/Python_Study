# Encapsulation (access modifiers: public, protected, private)
# Python DOES NOT HAVE access modifiers
# But we can follow the following conventions
# (no underscore) = public
# can be used anywhere
# _ (an underscore) = protected
# MUST not be used outside the class
# or its subclasses.
# __ (two underscores) = private
# "name mangling" in Python
# _ClassName__attr_name_or_method
# MUST only be used in the class in which it was
# declared.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'this is public'
        self._protected = 'this is protected'
        self.__example = 'this is private'

    def public_method(self):
        # self._method_protected()
        # print(self._protected)
        print(self.__example)
        self.__method_private()
        return 'public_method'

    def _method_protected(self):
        print('_method_protected')
        return '_method_protected'

    def __method_private(self):
        print('__method_private')
        return '__method_private'


f = Foo()
# print(f.public)
print(f.public_method())