# Understanding and using set datatype: https://www.w3schools.com/python/python_sets.asp
fruitSet = {"apple", "banana", "pineapple", "guava", "pineapple", "mango", "banana"}

print(fruitSet)

for x in fruitSet:
    print(x)

# Functions in set
fruitSet.add("orange")
print(fruitSet)

thisset = {"apple", "banana", "cherry"}
fruitSet.update(thisset)
print("updated set ", fruitSet)

# other functions like len, remove, discard, pop
# Few more functions Union, clear, difference, intersection, symmetric_difference_update