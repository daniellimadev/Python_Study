# Exercise - Postponing execution of functions
def sum(x, y):
    return x + y


def multiplies(x, y):
    return x * y


def create_function(function, x):
    def internal(y):
        return function(x, y)
    return internal 


sum_with_five = create_function(sum, 5)
multiply_by_ten = create_function(multiplies, 10)

print(sum_with_five(10))
print(multiply_by_ten(10))