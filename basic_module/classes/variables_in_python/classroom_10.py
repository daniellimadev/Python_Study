# An introduction to f-strings (string formatting)

name = 'Daniel Pereira'
height = 1.72
Weight = 74
bmi = Weight / height ** 2

"f-strings"
line_1 = f'{name} is {height:.2f} tall,'
line_2 = f'weighs {Weight} kilos and his BMI is'
line_3 = f'{bmi:.2f}'

print(line_1)
print(line_2)
print(line_3)

# Daniel Pereira is 1.72 tall,
# weighs 74 kilos and his BMI is
# 25.013520822065985

# Formatting strings with the format method
print()
print('Using another way to format the string!!\n')

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={name2} a={name1} a={name1} c={name3:.2f}'
format = string.format(
    name1=a, name2=b, name3=c
)

print(format)