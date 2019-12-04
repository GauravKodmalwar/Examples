"""
Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators
"""

# Arithmetic Operators

a = 22
b = 7
print("********** arithmatic **********")
print("addition of two vars is ", a + b)
print("subtraction of two vars is ", a - b)
print("division of two vars is ", a/b)
print("multiplication of two vars is ", a*b)
print("remainder after division of two vars is ", a%b)
print("quotient after division of two vars is ", a//b)
print("power of one vars to another is ", a**b)

# Comparison (Relational) Operators
print("********** Comparison or Relational **********")
print("is True == True, ", True==True)
print("is True != False, ", True!=False)
#print("is True <> True, ", a <> b)
print("is 5 > 3, ", 5 > 3)
print("is 5 < 3, ", 5 < 3)
print("is 5 >= 3, ", 5 >= 3)
print("is 5 <= 3, ", 5 <= 3)

print("********** Assignment Operators **********")
a = b + 5
a /= 2
b *= 1
a //= 2
b **= 3
b //= a
a %= b
print(a, b)

print("********** Bitwise Operators **********")
a = 60 #0b00111100
b = 13 #0b00001101
print(bin(22))

print("binary AND operator", a&b)
print("binary OR operator", a|b)
print("binary XOR operator", a^b)
print("binary negate or flipping bits operator", ~a)
print("binary left shift", a << 2)
print("binary right shift", b >> 2)

print("********** Logical Operators **********")
print(b and a)
print(b or a)
print(not(a and b))

print("********** Membership Operators **********")
print("in or not in")

print("********** Identity Operators **********")
print("is or is not")

# Operator precedence is very well explained here: https://www.tutorialspoint.com/python/python_basic_operators.htm

#Practice example: Write a code to convert 1) Decimal to binary. 2) Binary to Decimal