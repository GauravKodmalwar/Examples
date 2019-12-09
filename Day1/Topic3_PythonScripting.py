# White spaces are indentation either space or tabs

# line termination is typically a new line or Enter. Python is very much particular
# about indentation like new line or spaces or tabs

# Single line comments are created using hash ==> #

"""
Multi line comments are generated in blocks
"""

# Basic output in Python
print("Hello")

# whitespace in python or also called Indentation
# In some languages its called blocks like () or {}
# In python, any number of space or spaces can be whitespace
# It has to be equal in number for code in same line
if(False):
    print("Sucess")
else:
    print("Failed")


# Line termination in Python
print("This topic will show, how to print a new line in Python and using it, you can also understand the purpose of it. Sometimes, "
      "you may need to add new line in output")

print('In Python, even "single quotes" can be used ')

print("This topic will show, how to print a new line in Python and using it, you can also understand the purpose of it. Sometimes, \r\n"
      "you may need to add new line in output")

# Simple user input can be with function input, thats it. :)
age = input("enter your age")
print("your age is " + age + " years")

# Module is just a python file with .py extension
# It can contain, variable or clsses or function or code
import myModule
myModule.sayHello("Gaurav", "Pythoner")


# Module Search path
# Current directory then sys.path
# Now sys module is not here in current directory, its imported from site-packages
import sys
print("System search path can be found here: \n", "\n".join(sys.path))

import json
print(json.__file__)