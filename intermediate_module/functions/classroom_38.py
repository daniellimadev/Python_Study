# Combinations, Permutations and Product - Itertools
# Combination - Order doesn't matter - iterable + group size
# Permutation - Order matters
# Product - Order matters and repeats unique values
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


people = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
shirts = [
    ['black', 'white'],
    ['p', 'm', 'g'],
    ['male', 'female', 'unisex'],
    ['cotton-polyester']
]

print_iter(combinations(people, 2))
print_iter(permutations(people, 2))
print_iter(product(*shirts))