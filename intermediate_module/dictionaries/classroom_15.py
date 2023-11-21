# Dictionary Comprehension e Set Comprehension
product = {
    'name': 'Blue Pen',
    'price': 2.5,
    'category': 'Office',
}

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
    if key != 'category'
}

list = [
    ('a', 'value a'),
    ('b', 'value a'),
    ('b', 'value a'),
]
dc = {
    key: value
    for key, value in list
}

s1 = {2 ** i for i in range(10)}
print(s1)



