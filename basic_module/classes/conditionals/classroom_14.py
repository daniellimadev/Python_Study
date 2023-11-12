# Logical operators
# and (and) or (or) not (not)
# and - All conditions must be
# true.
# If any value is considered false,
# the entire expression will be evaluated at that value
# They are considered falsy (which you have already seen)
#0 0.0 '' False
# There is also the None type which is
# used to represent a non-value
# input = input('[E]Enter [Exit]Exit: ')
# entered_password = input('Password: ')

# allowed_password = '123456'

# if input == 'E' and password_entered == password_allowed:
# print('Enter')
#else:
# print('Quit')

# Short circuit assessment
print(True and False and True)
print(True and 0 and True)