# Enum -> Enumerations
# Enumerations in programming are used on occasions where we have
# a given number of things to choose from.
# Enums have members and their values ​​are constant.
# Enums in python:
# - are a set of symbolic names (members) linked to unique values
# - can be iterated to return their canonical members in the order of
# definition
# enum.Enum is the superclass for your enumerations. But it can also be used
# directly (even then, Enums are not normal classes in Python).
# You can use your Enum with type annotations, with isinstance and
# other type related things.
# To get the data:
# member = Class(value), Class['key']
#key = Class.key.name
# value = Class.key.value

import enum

# def move(direction):
#     print(f'Moving to {direction}')
# # Directions = enum.Enum('Directions', ['LEFT', 'RIGHT'])

# move('left')
# move('right')
# move('up')
# move('down')

class Directions(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    ABOVE = enum.auto()
    BELOW = enum.auto()


print(Directions(1), Directions['LEFT'], Directions.LEFT)
print(Directions(1).name, Directions.LEFT.value)


def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Direction not found')

    print(f'Moving to {direction.name} ({direction.value})')


move(Directions.LEFT)
move(Directions.RIGHT)
move(Directions.ABOVE)
move(Directions.BELOW)