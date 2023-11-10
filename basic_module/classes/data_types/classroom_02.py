# The print function

# \r\n -> CRLF
# \n -> LF

print(12, 34, sep="-", end='\r\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
print('')

"""
DocString
Python = Programming language
Typing type = Dynamic / Strong
str -> string -> text
Strings are texts that are enclosed in quotation marks
"""
print(1234)

# Single quotes
print('Daniel Pereira')
print(1, 'Daniel "Pereira"')

# Double quotes
print("Daniel Pereira")
print(2, "Daniel 'Pereira'")

# Escape
print("Daniel \"Pereira\"")

# r
print(r"Daniel \"Pereira\"")