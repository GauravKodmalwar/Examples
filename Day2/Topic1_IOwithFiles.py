"""
“ r “, for reading.
“ w “, for writing.
“ a “, for appending.
“ r+ “, for both reading and writing
"""

# Opening files: https://www.geeksforgeeks.org/file-handling-python/
file = open('pythonIO.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print(each)
print(type(file))

# Explore other functions read, readable, readline, readlines, seek, seekable, write, writelines
print(file.read())

# Working with files


# Controlling output location

