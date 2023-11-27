import json

person = {
    'name': 'Daniel',
    'surname': 'Pereira',
    'Adresses': [
        {'street': 'R1', 'number': 32},
        {'street': 'R2', 'number': 55},
    ],
    'height': 1.8,
    'preferred_numbers': (2, 4, 6, 8, 10),
    'dev': True,
    'nothing': None,
}

with open('classroom_45.json', 'w', encoding='utf8') as file:
    json.dump(
        person,
        file,
        ensure_ascii=False,
        indent=2,
    )

with open('classroom_45.json', 'r', encoding='utf8') as file:
    person = json.load(file)
    # print(person)
    # print(type(person))
    print(person['name'])