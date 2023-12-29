# Relations between classes: association, aggregation and composition
# Composition is a specialization of aggregation.
# But in it, when the "parent" object is deleted, all
# child object references are also
# deleted.
class Client:
    def __init__(self, name):
        self.name = name
        self.address = []

    def insert_address(self, street, number):
        self.address.append(Address(street, number))

    def insert_external_address(self, address):
        self.address.append(address)

    def list_address(self):
        for address in self.address:
            print(address.street, address.number)

    def __del__(self):
        print('DELETING,', self.name)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print('DELETING,', self.street, self.number)


client1 = Client('Maria')
client1.insert_address('Av Brasil', 54)
client1.insert_address('Rua B', 6745)
external_address = Address('Av Saudade', 123213)
client1.insert_external_address(external_address)
client1.list_address()

del client1


print(external_address.street, external_address.number)
print('######################## HERE ENDS MY CODE')