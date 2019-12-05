#List are mutable
"""
Lists are one of the four built-in data structures in Python, together with tuples, dictionaries, and sets.
They are used to store an ordered collection of items, which might be of different types but usually they aren't.
Commas separate the elements that are contained within a list and enclosed in square brackets.
"""
varList = [2, 3, 5 , 15.2]
print(id(varList))
varList[2] = "python"
print(id(varList))

# Common List method: https://www.programiz.com/python-programming/methods/list
varList.append(25)
varList.extend([24, 65, 77, 92])
print(varList)
print(varList.pop(3))
print(varList)
print(zip(varList))

# range function


# List operations
print("addition in list ", varList + [5])
print("multiplication in list ", varList * 2)

# String indexing
abc = "Python training"
for i in range(len(abc)):
    print(abc[i])

print(abc[5])

# String slicing
print(abc[4:9:-1])

# String iteration
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)
# fetch next value from iterator using next
print(next(my_iter))

print("print values using for loop")
for element in my_iter:
    print(element)

# Multi dimensional List: https://www.geeksforgeeks.org/multi-dimensional-lists-in-python/
a = [[2, 4, 6, 8 ], [ 1, 3, 5, 7 ], [ 8, 6, 4, 2 ], [ 7, 5, 3, 1 ]]

print("fetching list using one by one array ==> ")
for record in a:
    print(record)

print("print multi dimensional list using element by element")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()