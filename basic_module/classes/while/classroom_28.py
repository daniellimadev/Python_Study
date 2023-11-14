""" while/else """
string = 'Any Value'

i = 0
while i < len(string):
    letter = string[i]

    if letter == ' ':
        break

    print(letter)
    i += 1
else:
    print("I didn't find a space in the string.")
print('Outside of while.')