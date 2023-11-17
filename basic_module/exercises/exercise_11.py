"""
Make a shopping list with lists
The user must be able to
insert, delete and list values ​​from your list
Do not allow the program to break with
errors of non-existent indexes in the list.
"""
import os

list = []

while True:
    print('select an option')
    option = input('[i]insert [d]delete [l]list: ')

    if option == 'i':
        os.system('clear')
        value = input('Value: ')
        list.append(value)
    elif option == 'p':
        indice_str = input(
            'Choose the index to delete: '
        )

        try:
            indice = int(indice_str)
            del list[indice]
        except ValueError:
            print('Please enter int number.')
        except IndexError:
            print('Index does not exist in the list')
        except Exception:
            print('Unknown error')
    elif option == 'l':
        os.system('clear')

        if len(list) == 0:
            print('Nothing to list')

        for i, value in enumerate(list):
            print(i, value)
    else:
        print('Please choose i, a or l.')