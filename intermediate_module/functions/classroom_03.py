"""
Default values ​​for parameters
When defining a function, parameters can
have default values. If the value is not
sent to the parameter, the default value will be
used.
Refactor: edit your code.
"""


def sum(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


sum(1, 2)
sum(3, 5)
sum(100, 200)
sum(7, 9, 0)
sum(y=9, z=0, x=7)