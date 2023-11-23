# Introduction to lambda function (one-line anonymous function)
# The lambda function is a function like any
# another in Python. However, they are anonymous functions
# that contains only one line. That is, everything
# must be contained within a single
# expression.
# list = [
# {'name': 'Debora', 'surname': 'miranda'},
# {'name': 'Maria', 'surname': 'Oliveira'},
# {'name': 'Daniel', 'surname': 'Silva'},
# {'name': 'Eduardo', 'surname': 'Moreira'},
# {'name': 'Aline', 'surname': 'Souza'},
# ]
# list = [4, 32, 1, 34, 5, 6, 6, 21, ]
# list.sort(reverse=True)
# sorted(list)
list = [
    {'name': 'Debora', 'surname': 'miranda'},
    {'name': 'Maria', 'surname': 'Oliveira'},
    {'name': 'Daniel', 'surname': 'Silva'},
    {'name': 'Eduardo', 'surname': 'Moreira'},
    {'name': 'Aline', 'surname': 'Souza'},
]


def display(list):
    for item in list:
        print(item)
    print()


l1 = sorted(list, key=lambda item: item['name'])
l2 = sorted(list, key=lambda item: item['surname'])

display(l1)
display(l2)