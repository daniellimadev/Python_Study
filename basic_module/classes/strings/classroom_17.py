"""
Basic string interpolation
s - string
d e i - int
f - float
x and X - Hexadecimal (ABCDEF0123456789)
"""
name = 'Daniel'
price = 1000.95897643
variable = '%s, the price is R$%.2f' % (name, price)
print(variable)
print('The hexadecimal of %d is %08X' % (1500, 1500))