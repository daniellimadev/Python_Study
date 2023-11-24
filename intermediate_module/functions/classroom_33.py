# Decorator and decorator functions
# Decorate = Add / Remove / Restrict / Change
# Decorator functions are functions that decorate other functions
# Decorators are used to make Python
# use decorator functions in other functions.
# Decorators are "Syntax Sugar"

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


@create_function
def invert_string(string):
    print(f'{invert_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param must be a string')


inverted = invert_string('123')
print(inverted)