# Exemplo de uso dos sets
letters = set()
while True:
    letter = input('Type it: ')
    letters.add(letter.lower())

    if 'l' in letters:
        print('CONGRATULATIONS')
        break

    print(letters)