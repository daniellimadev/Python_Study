"""
Reps
while (while)
Performs an action while a condition is true
Infinite loop -> When a code has no end
"""
qty_lines = 5
qty_columns = 5

line = 1
while line <= qty_lines:
    column = 1
    while column <= qty_columns:
        print(f'{line=} {column=}')
        column += 1
    line += 1


print("It's over")