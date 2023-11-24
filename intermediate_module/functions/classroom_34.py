# Order of decorators
def parametros_decorador(name):
    def decorator(func):
        print('Decorator:', name)

        def your_new_function(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name}'
            return final
        return your_new_function
    return decorator


@parametros_decorador(name='5')
@parametros_decorador(name='4')
@parametros_decorador(name='3')
@parametros_decorador(name='2')
@parametros_decorador(name='1')
def sum(x, y):
    return x + y


ten_plus_five = sum(10, 5)
print(ten_plus_five)