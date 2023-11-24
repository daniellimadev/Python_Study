# Free variables + nonlocal (locals, globals)
# print(globals())
# def out(x):
# a = x

# def in():
# # print(locals())

# return a
# return inside


# inside1 = outside(10)
# in2 = out(20)

# print(in1())
# print(in2())
def concatenate(initial_string):
    end_value = initial_string

    def internal (value_to_concatenate=''):
        nonlocal end_value
        end_value += value_to_concatenate
        return end_value
    return internal 


c = concatenate('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)