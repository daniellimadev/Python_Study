# Relations between classes: association, aggregation and composition
# Aggregation is a more specialized form of association
# between two or more objects. Each object will have
# its independent life cycle.
# It is usually a one-to-many relationship, where one
# object has one or many objects.
# Objects can live separately, but can
# it is a relationship where an object needs
# another to do a certain task.
# (there are controversies about aggregation definitions).
class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])

    def insert_products(self, *products):
        # self._products.extend(products)
        # self._products += products
        for product in products:
            self._products.append(product)

    def list_products(self):
        print()
        for product in self._products:
            print(product.name, product.price)
        print()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
p1, p2 = Product('Pen', 1.20), Product('T-shirt', 20)
cart.insert_products(p1, p2)
cart.list_products()
print(cart.total())