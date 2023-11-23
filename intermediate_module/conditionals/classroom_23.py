# dir, hasattr and getattr in Python
string = 'Daniel'
method = 'strip'

if hasattr(string, method):
    print('There is upper')
    print(getattr(string, method)())
else:
    print('Method does not exist', method)