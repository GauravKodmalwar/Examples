"""
'r'	This is the default mode. It Opens file for reading.
'w'	This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.
'x'	Creates a new file. If file already exists, the operation fails.
'a'	Open file in append mode. If file does not exist, it creates a new file.
't'	This is the default mode. It opens in text mode.
'b'	This opens in binary mode.
'+'	This will open a file for reading and writing (updating)
"""

# Opening files: https://www.geeksforgeeks.org/file-handling-python/
file = open('pythonIO.txt', 'r')
# This will print every line one by one in the file

for each in file:
    print(each)
print(type(file))

# Explore other functions read, readable, readline, readlines, seek, seekable, write, writelines
print(file.read())

# Working with files: https://www.tutorialspoint.com/python/file_seek.htm
file.seek(0,0) # sets pointer on a file to the mentioned position. First number tells position and second tells from start or end of the file
print(file.read())
file.close()

file = open('pythonIO_write.txt', 'w')   # open('pythonIO_write.txt', 'a') ==> For appending content to a file, not to overwrite a file.
for i in range(5):
    file.write("python IO example, writting at line number {} \r\n".format(i))
file.close()

file = open('pythonIO_write.txt', 'r')
print(file.read())
file.close()

# Controlling output location
file = open("C:\\Temp\\PythonIO.txt", 'w')
file.write("Good morning")
file.close()

# import csv: https://www.programiz.com/python-programming/writing-csv-files

# writing to an excel, use below modules.
# import xlwt
# from xlwt import Workbook https://www.geeksforgeeks.org/writing-excel-sheet-using-python/

