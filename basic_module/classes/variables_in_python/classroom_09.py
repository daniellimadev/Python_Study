# Precedence between arithmetic operators

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
account_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(account_1)