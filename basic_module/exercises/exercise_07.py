""" Calculator with while """
while True:
    number_1 = input('Enter a number: ')
    number_2 = input('Enter another number: ')
    operator = input('Enter operator (+ - / *): ')

    valid_numbers = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or both of the numbers entered are invalid.')
        continue

    allowed_operators = '+-/*'

    if operator not in allowed_operators:
        print('Invalid operator.')
        continue

    if len(operator) > 1:
        print('Enter just one operator.')
        continue

    ###

    print("Registering your account. Check the result below:")

    if operator == '+':
        print(f'{num_1_float} + {num_2_float}= ',num_1_float + num_2_float)

    elif operator == '-':
        print(f'{num_1_float} - {num_2_float}= ',num_1_float - num_2_float)

    elif operator == '/':
        print(f'{num_1_float} / {num_2_float}= ',num_1_float / num_2_float)

    elif operator == '*':
        print(f'{num_1_float} * {num_2_float}= ',num_1_float * num_2_float)
    else:
        print('It should never get here.')

    exit = input('Do you want to exit? [y]yes: ').lower().startswith('y')

    if exit is True:
        break