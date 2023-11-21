# Manipulating keys and values ​​in dictionaries
person = {}

##
##

key = 'name'

person[key] = 'Daniel'
person['surname'] = 'Pereira'


print(person[key])

person[key] = 'Maria'

del person['surname']
print(person)
print(person['name'])

# print(person.get('surname'))
if person.get('surname') is None:
    print('DOES NOT EXIST')
else:
    print(person['last name'])

# print('THIS WON'T')
print(person, type(person))