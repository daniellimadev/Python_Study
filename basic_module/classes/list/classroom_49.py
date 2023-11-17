# Unpacking in calls
# of methods and functions
string = 'ABCD'
list = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tuple = 'Python', 'is', 'cool'
rooms = [
    #0 1
    ['Maria', 'Helena', ], #0
    #0
    ['Elaine', ], #1
    #0 1 2
    ['Luiz', 'João', 'Eduarda', ], #2
]

# p, b, *_, ap, u = list
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*list)
# print(*string)
# print(*tuple)

print(*rooms, sep='\n')