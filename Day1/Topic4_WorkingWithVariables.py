# Python variables

# UNIQUE feature in Python is "No declaration"
x = 20
y = 20.45
z = "Gaurav"

print("Integer {0} and float {1} and string {2}".format(x, y , z))
print("Type {0} and Type {1} and Type {2}".format(type(x), type(y) , type(z)))

# Variable naming convention
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
dfd155_ = 20

# All default variables in Python are Objects with class as 'int', 'float' and 'str'
print("Valid variable naming conventions has value {0}".format(dfd155_))

# Variable reference and Garbage collection

import sys, gc
abc = 1
bac = abc
cab = bac

print(sys.getrefcount(abc))
# *******************Output is wrong, have to research further

del abc

# help(sys.getrefcount)

# Garbage collection in Python called as "Generational Garbage Collection"
"""
https://stackify.com/python-garbage-collection/

Python has 3 levels of garbage collection
1) Youngest generation 
2) Current generation
3) Old generation
"""

import gc
print("Current GC threshold in terms of number of objects ", gc.get_threshold())
print("Current objects count before GC ", gc.get_count())
gc.collect()
print("Current objects count after GC ", gc.get_count())

#You can modify GC setting to appear as per convinient
gc.set_threshold(1000, 15, 15)

# Sequence type
# Sequence Types -- str, unicode, list, tuple, buffer, xrange
#https://www.unicode.org/
#https://docs.python.org/3/howto/unicode.html

xyz = '\u0394'
print("value of unicode is {} and type is {}".format(xyz, type(xyz)))

xyz = '\u0063'
print("value of unicode is {} and type is {}".format(xyz, type(xyz)))

# List ==> Lists are constructed with square brackets, separating items with commas: [a, b, c]
# https://www.geeksforgeeks.org/python-list/
varList = [1,2,3]
print(varList)

varList = [3, 'akshay', 'sneha', 'deepika']
print(varList)
print(type(varList))
print(type(varList[0]))
varList = [14.6, 26.7, 20.34]
print(varList)

varList2 = [[]] * 3
print(varList2)
#varList2.append(15)
print(varList2)
varList2[0].append(15)
print(varList2)

# Tuple ==> Tuples are constructed by the comma operator, with or without enclosing parentheses
# https://www.w3schools.com/python/python_tuples.asp
varTuple = (12, 40, 22)
print(varTuple)
print(type(varTuple))
print(varTuple[0])
print((4, 'dfda', 535) + (12, 'gaurav', 25))

# buffers are replaced by the memoryview in python 3: https://docs.python.org/3/c-api/memoryview.html
# xrange is deprecated in python 3: https://www.geeksforgeeks.org/range-vs-xrange-python/

# Membership statement: https://www.tutorialspoint.com/python/membership_operators_example.htm

a, b = 20, 35
varList3 = [20, 50, 22]

print(a in varList3)
print(b in varList3)
print(a not in varList3)

print(a is int)
print(varList3 is not int)

# List iteration: https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
list = [1, 3, 5, 7, 9]
# Using for loop
print("Using for loop")
for i in list:
    print(i)

# Iterating the index
# same as 'for i in range(len(list))'
print("Using len and range function")
length = len(list)
for i in range(length):
    print(list[i])

# Using while loop
print("Using while loop")
i = 0
while i < length:
    print(list[i])
    i += 1

# Using list comprehension
print("Using list comprehension")
[print(i) for i in list]

# simple assignment and logical operators ***interesting*** https://docs.python.org/3/reference/simple_stmts.html


# Mutable vs immutable Objects: https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/
#Immutable Objects : These are of in-built types like int, float, bool, string, unicode, tuple.
"""
Mutable and immutable objects are handled differently in python. Immutable objects are quicker to access and are expensive to change because it involves the creation of a copy.
Whereas mutable objects are easy to change.
Use of mutable objects is recommended when there is a need to change the size or content of the object.
"""
tuple1 = (0, 1, 2, 3)
#tuple1[0] = 4
print(tuple1)

message = "Welcome to GeeksforGeeks"
#message[0] = 'p'
print(message)

#Mutable Objects : These are of type list, dict, set.
# lists are mutable
color = ["red", "blue", "green"]
color[0] = "pink"
color[-1] = "orange"
print(color)

# woraround for immutable objects
tup = ([1,2,3,4], 'gaurav')
tup[0].append(25)
print(tup)

# Multi target assignments
a, b, c = 4, "gaurav", 24.5
print("printed from multi target assignment {}, {}, {}".format(a, b, c))

