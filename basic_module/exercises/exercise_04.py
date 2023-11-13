# Exercise: test your knowledge so far

"""
Exercise
Ask the user to enter their name
Ask the user to enter their age
If name and age are entered:
    Display:
        Your name is {name}
        Your reversed name is {reversed name}
        Your name contains (or does not contain) spaces
        Your name has {n} letters
        The first letter of your name is {letter}
        The last letter of your name is {letter}
If nothing is entered for name or age:
    display "Sorry, you left fields empty."
"""
name = input('Enter your name: ')
age = input('Enter your age: ')

if name and age:
    print(f'Your name is {name}')
    print(f'Your reversed name is {name[::-1]}')

    if ' ' in name:
        print('Your name contains spaces')
    else:
        print('Your name does NOT contain spaces')

    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is {name[0]}')
    print(f'The last letter of your name is {name[-1]}')
else:
    print("Sorry, you left fields empty.")