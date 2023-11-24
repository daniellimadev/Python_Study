# Standard Python modules (import, from, as and *)
# https://docs.python.org/3/py-modindex.html
# integer - import module_name
# Advantages: you have the module namespace
# Disadvantages: big names
# import sys

# platform = 'MINE'
# print(sys.platform)
# print(platform)

# parts - from module_name import object1, object2
# Advantages: small names
# Disadvantages: No module namespace
# from sys import exit, platform

# print(platform)

# alias 1 - import module_name as nickname
# import sys as s

# sys = 'something'
# print(s.platform)
# print(sys)


# alias 2 - from module_name import object as nickname
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Advantages: you can reserve names for your code
# Disadvantages: may be outside the language standard

# bad practice - from module_name import *
# Advantages: import everything from one module
# Disadvantages: imports everything from one module
# from sys import exit, platform

# print(platform)
#exit()