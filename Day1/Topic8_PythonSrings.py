# Generating random strings: https://www.geeksforgeeks.org/python-generate-random-string-of-given-length/
import string
import random
import secrets

print(''.join(random.choices(string.ascii_uppercase + string.digits, k= 10)))

res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(15))
print(res)

# Immutable
abc = "Python Training"
#abc[0] = "a"
print(id(abc))
abc = "Immutable check"
print(id(abc))

# Common string functions in python: https://www.programiz.com/python-programming/methods/string

xyz = "Python string training"
print("lower {} and upper {} strings".format(xyz.lower(), xyz.upper()))
print(xyz.join(" *** "))
print(xyz.split((" ")))
print(xyz.find("string"))
print(xyz.replace("a", "A"))

# Type conversion in Python: https://www.geeksforgeeks.org/type-conversion-python/
print("converted string to integer ", int("2"))
print("converted string to float ", float("2.56"))
print("converted string to integer ", ord('0'))
print("converted string to integer of base 2 = ", int("010111", 2))

# String formatting: https://www.learnpython.org/en/String_Formatting
name, age = "John", 23
print("%s is %d years old." % (name, age))
tokens = [2, 4, 6, 9]
print("Tokens are %s" % tokens)

# Variable substitution
print(f"{name} is {age} years old.")

# String Indexing
print("5th value in xyz string is ", xyz[5])

# String slicing
print("value of xyz = ", xyz)
print("values in xyz string from 5th index is ", xyz[5:])
print("values in xyz string from 5th to 10th index is ", xyz[5:10])
print("values in xyz string upto 8th index is ", xyz[:8])
print("Stride with slicing: ", xyz[6: 20: 2])
print("reverse string is ", xyz[::-1])

# String Iteration
# already seen example of "for i in xyz"
# already seen example of "for i in range(len(xyz))
for i,v in enumerate(xyz):
    print(v)