# function basics
"""
Step 1: Declare the function with the keyword def followed by the function name.
Step 2: Write the arguments inside the opening and closing parentheses of the function, and end the declaration with a colon.
Step 3: Add the program statements to be executed.
"""

def my_function():
  print("*** Hello from a function ***")
my_function()

def my_function2(name):
  print("*** Hello {}, from a function ***".format(name))

my_function2("Gaurav")

# Function polymorphism
def my_function(name):
  print("*** Hello {}, from a function ***".format(name))

def my_function(name, age):
  print("*** Hello {}, from a function. Your age is {} ***".format(name, age))

my_function("Gaurav", 30)

# Argument defaults. Argument assignment happens with = sign to a argument. https://www.geeksforgeeks.org/polymorphism-in-python/
def my_function(name, age, gender="male"):
  print("*** Hello {}, from a function. Your age is {}. Your gender is {} ***".format(name, age, gender))

my_function("Gaurav", 30)
my_function("Gaurav", 30, "female")

# Lambada function
"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

# Local variables: https://www.geeksforgeeks.org/global-local-variables-python/
def f():
  print(s)
s = "I love Python"
f()

# Global and local variables
def f():
  s = "Me too."
  print(s)
s = "I love Python"
print(s)
f()

# Global and local overlap

# This will give error ==> UnboundLocalError: local variable 's' referenced before assignment
"""
def f():
  print(s)
  s = "Me too."
  print(s)
s = "I love Python"
print(s)
f()
"""

def f():
  global s
  print(s)
  s = "Me too."
  print(s)
s = "I love Python"
print(s)
f()


# all list of builtin functions: https://docs.python.org/3/library/functions.html
# all list of builtin functions: https://www.w3schools.com/python/python_ref_functions.asp

# Understanding __builtin__ : https://docs.python.org/2/library/__builtin__.html
"""
This module provides direct access to all 'built-in' identifiers of Python; 
for example, __builtin__. open is the full name for the built-in function open() .
"""
import builtins

def open(path):
    f = builtins.open(path, 'r')
    return UpperCaser(f)

class UpperCaser:
    '''Wrapper around a file that converts output to upper-case.'''

    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        return self._f.read(count).upper()

print(open('pythonIO.txt').read())

# preventing variable modification
"""
A constant is a type of variable that holds values, which cannot be changed. 
In reality, we rarely use constants in Python. 
Constants are usually declared and assigned on a different module/file. Then, they are imported to the main file.
"""
import constants
print(constants.PI)
print(constants.WEEKLY_DAYS)
print(constants.NUMBER_OF_MONTHS)

# Argument matching methods

#Keyword argument methods

