def execute(function, *args):
    return function(*args)


# def sum(x, y):
# return x + y


# def create_multiplier(multiplier):
# def multiply(number):
# return number * multiplier
# return multiply


# duplicate = creates_multiplier(2)
duplicate = execute(
    lambda m: lambda n: n * m,
    2
)
print(duplicate(2))

print(
    execute(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    execute(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)