# About exceptions : https://www.pythonforbeginners.com/error-handling/exception-handling-in-python
"""
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions.
In general, when a Python script encounters a situation that it cannot cope with, it raises an exception.
An exception is a Python object that represents an error.
"""
# 5 / 0

# Learn how exceptions work in Python : https://www.geeksforgeeks.org/python-set-5-exception-handling/
# Handling exception
# Raising exception
# Catching exception

# How to raise an exception and how to handle it ==>
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")

# Default exception handler
try:
    open("PythonReserch", 'r')
except Exception as e:
    print("Problem opening a file {0}".format(str(e)))

# Try/Except/Else/Finally exceptions
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    finally:
        print("The code in the finally block will be executed regardless of whether an exception occurs.")
        print("******* Excellent Job *******")

AbyB(5, 7)

# Generating user defined exceptions: https://www.geeksforgeeks.org/user-defined-exceptions-python-examples/
class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "OMG, value is {}".format(self.value)

try:
    raise (MyError(3 * 2))

# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occured: ', str(error))

# Using Asserts ==> asserts are used to validate expression to return True or False. https://airbrake.io/blog/python-exception-handling/python-assertionerror
a = 20
b = 20

assert a!=b

# Exception classes: https://www.geeksforgeeks.org/built-exceptions-python/
# ArithmeticError
# BufferError
# LookupError
# AssertionError
# IndexError
