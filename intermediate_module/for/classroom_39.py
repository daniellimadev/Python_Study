# groupby - grouping values ​​(itertools)
from itertools import groupby

students = [
    {'name': 'Daniel', 'note': 'A'},
    {'name': 'Letícia', 'note': 'B'},
    {'name': 'Fabrício', 'note': 'A'},
    {'name': 'Rosemary', 'note': 'C'},
    {'name': 'Joana', 'note': 'D'},
    {'name': 'John', 'note': 'A'},
    {'name': 'Eduardo', 'note': 'B'},
    {'name': 'André', 'note': 'A'},
    {'name': 'Anderson', 'note': 'C'},
]


def order(student):
    return student['note']


grouped_students = sorted(students, key=order)
groups = groupby(grouped_students, key=order)

for key, group in groups:
    print(key)
    for student in group:
        print(student)