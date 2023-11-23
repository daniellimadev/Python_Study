# try, except, else and finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('OPEN FILE')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVID ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('No error')
finally:
    print('CLOSE FILE')