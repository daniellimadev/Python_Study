import os

# Creating files with Python + Context Manager with
# We use the open function to open
# a Python file (it may or may not exist)
# Modes:
# r (read), w (write), x (for creation)
# a (writes at the end), b (binary)
# t (text mode), + (reading and writing)
# Context manager - with (opens and closes)
# Useful methods
# write, read (write and read)
# writelines (write multiple lines)
# seek (moves the cursor)
# readline (read line)
# readlines (read lines)
# Let's talk more about the os module, but:
# os.remove or unlink - deletes the file
# os.rename - change the name or move the file
# Let's talk more about the json module, but:
# json.dump = Generates a json file
# json.load
file_path = 'C:\\Users\\danie\\Documents\\Python_Study\\intermediate_module\\creating_files_context_manager\\'
file_path += 'clasroom_44.txt'

# file = open(file_path, 'w')
# #
# file.close()
# with open(file_path, 'w') as file:
#     print('Hello world')
#     print('File will be closed')

# with open (context manager) and useful TextIOWrapper methods

# with open(file_path, 'w+') as file:
#     file.write('Line 1\n')
#     file.write('Line 2\n')
#     file.writelines(
#         ('Line 3\n', 'Line 4\n')
#     )
#     file.seek(0, 0)
#     print(file.read())
#     print('Reading')
#     file.seek(0, 0)
#     print(file.readline(), end='')
#     print(file.readline().strip())
#     print(file.readline().strip())

#     print('READLINES')
#     file.seek(0, 0)
#     for line in file.readlines():
#         print(line.strip())


# print('#' * 10)

# with open(file_path, 'r') as file:
#     print(file.read())


with open(file_path, 'w+') as file:
    file.write('Atenção\n')
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.writelines(
        ('Line 3\n', 'Line 4\n')
    )
    
# os.remove(file_path) # or unlink
# os.remove(file_path, 'classroom_44.txt')
