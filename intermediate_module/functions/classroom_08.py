def twice(f):
    def result(x):
        return f(f(x))
    return result
@twice
def g(i):
    return i + 3

g(7)

print(g(7))