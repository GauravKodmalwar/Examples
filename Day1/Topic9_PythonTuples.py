# Immutable : https://www.w3schools.com/python/python_tuples.asp
"""
Tuples are used for grouping data
A tuple lets us “chunk” together related information and use it as a single thing.
Tuples support the same sequence operations as strings. ... So like strings, tuples are immutable.
Once Python has created a tuple in memory, it cannot be changed.
"""
varTuple = (5, 20, 40)
#varTuple[0] = 5  # TypeError: 'tuple' object does not support item assignment
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Common tuples methods
thistuple = ("apple", "banana", "cherry")
print("count function returns the number of counts in tuples = ", thistuple.count("apple"))
print("index returns the index of object in a tuple = ", thistuple.index("cherry"))

#Tuples operations: https://www.geeksforgeeks.org/tuples-in-python/
a = (3, 56, 20, 10)
b = (12.4, 567.2, 565.357)
print("addition of tuples ", a + b)
print("multiplication of tuples ", a * 5)
print("smalles number in tuple: ", min(b))

del a
#print(a)

a, b, c = varTuple
print("multi assignment in Python")
print(a, b, c)

#Tuples indexing
print("Indexing tuple just like list")
print(thistuple[1])

#Tuples slicing
print("tuple values after reversing using slicing: ", thistuple[::-1])

#Tuples iteration
for i in range(len(thistuple)):
    print(thistuple[i])

#Multi dimensional tuples
multiTuples = ((25, 60), ("tuple1", "tuple2"))
print(multiTuples)
print(multiTuples[1])

"""
************* Difference between list and tuple *************
1) List is mutable i.e once created then we can modify its contents. Whereas, a Tuple is immutable i.e. once created we can change its contents, therefore tuple doesn’t provide functions like append(), remove() etc.
2) As tuple is immutable, so we can use it as key in a dictionary too.
"""