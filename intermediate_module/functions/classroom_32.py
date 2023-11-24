# Decorator and decorator functions
# Decorate = Add / Remove / Restrict / Change
# Decorator functions are functions that decorate other functions
# Decorators are used to make Python
# use decorator functions in other functions.

def create_function(func):
    def internal (*args, **kwargs):
        print("I'll decorate you")
        for arg in args:
            e_string(arg)
        result = func(*args, **kwargs)
        print(f'Your result was {result}.')
        print('Ok, now you have been decorated')
        return result
    return internal 


def invert_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param must be a string')


invert_string_checking_parameter = create_function(invert_string)
inverted = invert_string_checking_parameter('123')
print(inverted)