# Problem with mutable parameters in Python functions
def adds_clientes(name, list=None):
    if list is None:
        list = []
    list.append(name)
    return list


client1 = adds_clientes('Daniel')
adds_clientes('Joana', client1)
adds_clientes('Fernando', client1)
client1.append('Edu')

client2 = adds_clientes('Helena')
adds_clientes('Maria', client2)

client3 = adds_clientes('Moreira')
adds_clientes('Vivi', client3)

print(client1)
print(client2)
print(client3)