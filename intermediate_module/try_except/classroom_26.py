# (Part1) try and except to handle exceptions
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    print('Line 1'[1000])
    c = a / b
    print('Line 2')
except ZeroDivisionError:
    print('Divided by zero.')
except NameError:
    print('Name b is not defined')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:
    print('UNKNOWN ERROR.')

print('CONTINUE')