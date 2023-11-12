# if, elif and else: understanding the interpreter flow in conditionals

# if / elif      / else
# if / else if  / if not

condition1 = True
condition2 = True
condition3 = True
condition4 = True

if condition1:
    print('Code for condition 1')
    print('Code for condition 1')
elif condition2:
    print('Code for condition 2')
elif condition3:
    print('Code for condition 3')
elif condition4:
    print('Code for condition 4')
else:
    print('No conditions were met.')

if 10 == 10:
    print('Another if')

print('Outside of if')