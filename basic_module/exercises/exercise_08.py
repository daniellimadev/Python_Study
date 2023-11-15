"""
Make a game for the user to guess which one
the secret word.
- You will propose a secret word
any and will give the possibility to
the user types only one letter.
- When the user types a letter, you
will check if the typed letter is
in the secret word.
    - If the letter entered is in the
    secret word; display the letter;
    - If the letter entered is not
    in the secret word; display *.
Count your attempts
user.
"""
import os

secret_word = 'Home'
correct_letters = ''
number_attempts = 0

while True:
    typed_letter = input('Enter a letter: ')
    number_attempts += 1

    if len(typed_letter) > 1:
        print('Enter just one letter.')
        continue

    if typed_letter in secret_word:
        correct_letters += typed_letter

    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in correct_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'

    print('Formed word:', formed_word)

    if formed_word == secret_word:
        os.system('clear')
        print('YOU WON!! CONGRATULATIONS!')
        print('The word was', secret_word)
        print('Attempts:', number_attempts)
        correct_letters = ''
        number_attempts = 0
        break