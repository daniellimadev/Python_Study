# Introduction to +if/elif/else (conditional) code blocks

# if / elif      / else
# if / else if  / if not
prohibited = input('You want "to enter" or "close"? ')

if prohibited == 'to enter':
    print('You have entered the system!!')

    print(12341234)
elif prohibited == 'close':
    print('You left the system...')
else:
    print("You didn't type in or out.")

print('OUT OF THE BLOCKS')