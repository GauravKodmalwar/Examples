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

# Keyword argument or named arguments methods: https://treyhunner.com/2018/04/keyword-arguments-in-python/
from math import sqrt

def quadratic(a, b, c):
  x1 = -b / (2 * a)
  x2 = sqrt(b ** 2 - 4 * a * c) / (2 * a)
  return (x1 + x2), (x1 - x2)

print(quadratic(31, 93, 62))
print(quadratic(62, 93, 31))
print(quadratic(a=31, b=93, c=62))
print(quadratic(c=62, a=31, b=93))

# Argument matching methods
# Unnamed argument matching function
"""
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. 
It is used to pass a non-keyworded, variable-length argument list.
"""
print("************** variable length and unnamed arguments **************")

def myFun(*argv):
  for arg in argv:
    print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def product(*numbers, initial=1):
  total = initial
  for n in numbers:
    total *= n
  return total

print(product(4, 6, initial=5))

"""
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
"""
print("************** variable length but named arguments **************")
def myFun(**kwargs):
  for key, value in kwargs.items():
    print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')

#arbitrary keyword arguments
print("************** without declaring variable keyword lengths in function definition **************")
def myFun(arg1, arg2, arg3):
  print("arg1:", arg1)
  print("arg2:", arg2)
  print("arg3:", arg3)

args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

"*********** yield ***********"