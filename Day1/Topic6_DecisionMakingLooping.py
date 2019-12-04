# Decision making in Python: https://www.geeksforgeeks.org/decision-making-python-else-nested-elif/

a = 15
b = 15

#IF
if(a == b):
    print("Numbers are equal")

# IF Else
if(False):
    pass
else:
    print("Numbers are not equal")

# Nested If else
c = "gaurav"
if(type(c) == str):
    pass
elif(True):
    print("Its not a string")
else:
    print("No condition matched")

# Ternary Operator: https://www.geeksforgeeks.org/ternary-operator-in-python/
a, b = 20, 10
min = a if a > b else b
print(min)

print( (b, a) [a > b] )
print({True: a, False: b} [a < b])
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")

min = a > b and a or b
print(min)

#While loop: https://www.w3schools.com/python/python_while_loops.asp
name = "gaurav"
i = 0
print("While loop example")
while(i < len(name)):
    if i > 2:
        break
    print(name[i])
    i+=1

#For loop: https://www.w3schools.com/python/python_while_loops.asp
print("For loop example")
for i in range(len(name)):
    if i < 3:
        continue
    print(name[i])