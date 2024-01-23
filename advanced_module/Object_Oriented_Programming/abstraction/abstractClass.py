# Abstract classes - Abstract Base Class (abc)
# ABCs are used as contracts for the definition
# of new classes. They can force other classes
# to create concrete methods. They may also have
# concrete methods by themselves.
# @abstractmethods are methods that have no body.
# The rules for abstract classes with methods
# abstract is that they CANNOT be instanced
# directly.
# Abstract methods MUST be implemented
# in subclasses (@abstractmethod).
# An abstract class in Python has its metaclass
# being ABCMeta.
# It is possible to create @property @setter @classmethod
# @staticmethod and @method as abstract, for this
# use @abstractmethod as the innermost decorator.
from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('Hi')
