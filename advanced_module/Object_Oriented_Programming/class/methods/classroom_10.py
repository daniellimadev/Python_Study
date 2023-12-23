# @staticmethod (static methods) are useless in Python =)
# Static methods are methods that are within the
# class, but does not have access to self or cls.
# In short, they are functions that exist within your
# class.
class Class:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Hi', args, kwargs)


def function(*args, **kwargs):
    print('Hi', args, kwargs)


c1 = Class()
c1.funcao_que_esta_na_classe(1, 2, 3)
function(1, 2, 3)
Class.funcao_que_esta_na_classe(named=1)
function(named=1)