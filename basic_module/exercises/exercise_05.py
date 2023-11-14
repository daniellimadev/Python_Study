"""
Write a program that asks the user to enter an integer,
Tell us if this number is even or odd. If the user does not enter a number
integer, inform that it is not an integer.
"""
input = input('Enter a number: ')

# if input.isdigit():
# input_int = int(input)
# odd_even = input_int % 2 == 0
# even_odd_text = 'odd'

# if odd_even:
# odd_even_text = 'even'

# print(f'The number {input_int} is {odd_even_text}')
#else:
# print('You did not enter an integer')

try:
    input_int = float(input)
    odd_even = input_int % 2 == 0
    odd_even_text = 'odd'

    if odd_even:
        odd_even_text = 'even'

    print(f'The number {input_int} is {odd_even_text}')
except:
    print('You did not enter an integer')
"""
Write a program that asks the user for the time and, based on the time
described, display the appropriate greeting. Ex.
Good morning 0-11, Good afternoon 12-17 and Good evening 18-23.
"""
"""
Write a program that asks for the user's first name. If the name has 4 letters or
less write "Your name is short"; if it has between 5 and 6 letters, write
"Your name is normal"; greater than 6 write "Your name is too long".
"""