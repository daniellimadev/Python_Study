# Exercises with functions

# Create a function that multiplies all arguments
# no nominees received
# Return the total to a variable and display the value
# of the variable.
def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total


multiplication = multiply(10, 2, 3, 4, 5)
print(multiplication)


# Create a function that tells whether a number is even or odd.
# Return whether the number is even or odd.
def even_odd(number):
    multiple_of_two = number % 2 == 0

    if multiple_of_two:
        return f'{number} is even'
    return f'{number} is odd'


other_even_odd = even_odd
two_and_even = other_even_odd(2)
print(two_and_even)
print(even_odd(3))
print(even_odd(15))
print(even_odd(16))

print(even_odd is other_even_odd)