# Logical operator "not"
# Used to invert expressions
# not True = False
# not False = True
# password = input('Password: ')
print(not True) # False
print(not False) # True

# Operators in and not in
# Strings are iterable
#0 1 2 3 4 5
# Tá v i o
# -6-5-4-3-2-1
# name = 'Otávio'
# print(name[2])
# print(name[-4])
# print('vio' in name)
# print('zero' in name)
# print(10 * '-')
# print('vio' not in name)
# print('zero' not in name)

name = input('Enter your name: ')
find = input('Enter what you want to find: ')

if find in name:
    print(f'{find} is in {name}')
else:
    print(f'{find} is not in {name}')