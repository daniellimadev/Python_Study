# Recursive functions and recursion
# - functions that can call themselves back
# - useful for dividing large problems into smaller parts
# Every recursive function must have:
# - A problem that can be broken down into smaller parts
# - A recursive case that solves the small problem
# - A base case that stops recursion
# - factorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
# import sys

def recursive(start=0, end=4):

    print(start, end)

    # Base case
    if start >= end:
        return end

    # Recursive case
    # count until reaching the end
    start += 1
    return recursive(start, end)


print(recursive())

# sys.setrecursionlimit(1004)

# def recursive(start=0, end=4):

# print(start, end)

# # Base case
# if start >= end:
# return end

# # Recursive case
# # count until you reach the end
# start += 1
# return recursive(start, end)

# print(recursive(0, 1001))
print()

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))