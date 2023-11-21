# Useful dictionary methods in Python
# len - how many keys
# keys - iterable with keys
# values ​​- iterable with values
# items - iterable with keys and values
# setdefault - adds value if key does not exist
# copy - returns a shallow copy (shallow copy)
# get - get a key
# pop - Deletes an item with the specified key (del)
# popitem - Deletes the last added item
# update - Updates one dictionary with another
p1 = {
    'name': 'Daniel',
    'surname': 'Pereira',
}
# print(p1['name'])
# print(p1.get('name', 'Does not exist'))

# name = p1.pop('name')
# print(name)
# print(p1)
# last_key = p1.popitem()
# print(last_key)
# print(p1)
# p1.update({
# 'name': 'new value',
# 'age': 30,
# })
# p1.update(name='new value', age=30)
# tuple = (('name', 'new value'), ('age', 30))
list = [['name', 'new value'], ['age', 30]]
p1.update(list)
print(p1)