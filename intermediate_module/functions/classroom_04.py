"""
Scope of Functions in Python
Scope means where that code can reach.
There is global and local scope.
The global scope is the scope where all code is reachable.
The local scope is the scope where only names from the same location
can be achieved.
"""

x = 1


def scope():
    global x
    x = 10

    def other_function():
        global x
        x = 11
        y = 2
        print(x, y)

    other_function()
    print(x)


print(x)
scope()
print(x)