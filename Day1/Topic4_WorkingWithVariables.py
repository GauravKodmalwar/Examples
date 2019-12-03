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



