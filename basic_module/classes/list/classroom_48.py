"""
List of lists and their indexes
"""
rooms = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Daniel', 'João', 'Eduarda', ],  # 2
]

# print(rooms[1][0])
# print(rooms[0][1])
# print(rooms[2][2])
# print(rooms[2][3][3])

for room in rooms:
    print(f'The room is {room}')
    for student in room:
        print(student)