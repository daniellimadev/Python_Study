import copy

from data.products_module import products

# copy, sorted, products.sort
# Exercises
# Increase the prices of the following products by 10%
# Generate new_products by deep copy
# products = [
# {'name': 'Product 5', 'price': 10.00},
# {'name': 'Product 1', 'price': 22.32},
# {'name': 'Product 3', 'price': 10.11},
# {'name': 'Product 2', 'price': 105.87},
# {'name': 'Product 4', 'price': 69.90},
# ]

new_products = [
    {**p, 'price': round(p['price'] * 1.1, 2)}
    for p in copy.deepcopy(products)
]

# print(*products, sep='\n')
#print()
# print(*new_products, sep='\n')

# Sort products by descending name (from largest to smallest)
# Generate products_ordered_by_name by deep copy
products_sorted_by_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['name'],
    reverse=True
)
# print(*products, sep='\n')
#print()
# print(*products_ordered_by_name, sep='\n')


# Sort products by increasing price (from lowest to highest)
# Generate ordered_products_by_price by deep copy
products_ordered_by_price = sorted(
    copy.deepcopy(products),
    key=lambda p: p['price']
)

# FINAL

print(*products, sep='\n')
print()
print(*new_products, sep='\n')
print()
print(*products_sorted_by_name, sep='\n')
print()
print(*products_ordered_by_price, sep='\n')