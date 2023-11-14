"""
Flag - Mark a location
None = No value
is and is not = is or is not (type, value, identity)
id = Identity
"""
condition = False
passed_no_if = None

if condition:
    passed_no_if = True
    print('Do something')
else:
    print("Don't do something")


if passed_no_if is None:
    print("Didn't pass if")
else:
    print('Passed if')