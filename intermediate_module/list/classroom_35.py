# In the previous exercise, we added two lists using several different solutions.

# One of them was using zip to join two lists and use list comprehension to do the math:

list_a = [10, 2, 3, 4, 5]
list_b = [12, 2, 3, 6, 50, 60, 70]
sum_list = [x + y for x, y in zip(list_a, list_b)]
print(sum_list) # Output: [22, 4, 6, 10, 55]
# The problem is that zip only joins the lists up to the size of the smallest list (as proposed in the exercise).

# Another possibility is to use zip_longest to capture the values ​​from the longer list.

# The idea is the same, see:

from itertools import zip_longest
 
list_a = [10, 2, 3, 4, 5]
list_b = [12, 2, 3, 6, 50, 60, 70]
sum_list = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)]
print(sum_list) # [22, 4, 6, 10, 55, 60, 70]
# In this case, we use the "fillvalue" as 0 (zero), so we can capture the remaining values ​​from the larger list, performing calculations, without getting an error in our program.