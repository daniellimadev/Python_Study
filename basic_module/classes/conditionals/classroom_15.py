# Logical operators
# and (and) or (or) not (not)
# or - Any true condition evaluates
# all expression as true.
# If any value is considered true,
# the entire expression will be evaluated at that value.
# They are considered falsy (which you have already seen)
#0 0.0 '' False
# There is also the None type which is
# used to represent a non-value

# input = input('[E]Enter [Exit]Exit: ')
# entered_password = input('Password: ')

# allowed_password = '123456'

# if (input == 'E' or input == 'e') and entered_password == allowed_password:
# print('Enter')
#else:
# print('Quit')

# Short circuit assessment
password = input('Password: ') or 'No password'
print(password)