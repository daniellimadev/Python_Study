"""
Named and unnamed arguments in Python functions
Named argument has name with equals sign
Unnamed argument takes only the argument (value)
"""


def sum(x, y, z):
    # Definition
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


sum(1, 2, 3)
sum(1, y=2, z=5)

print(1, 2, 3, sep='-')
