"""
args - Unnamed arguments
* - *args (packing and unpacking)
"""
# Remember unpacking
# x, y, *remainder = 1, 2, 3, 4
# print(x, y, remainder)


# def sum(x, y):
# return x + y
 
def sums(*args):
     total = 0
     for number in args:
        total += number
     return total
 
sum_1_2_3 = sums(1, 2, 3)
print(sum_1_2_3)

sum_4_5_6 = sums(4, 5, 6)
print(sum_4_5_6)

numbers = 1, 2, 3, 4, 5, 6, 7, 78, 10
other_sum = sums(*numbers)
print(other_sum)

print(sum(numbers))
# print(*numbers)