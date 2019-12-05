# Basic list comprehension
my_list = [4, 6, 9, 10]
new_list = []

for i in my_list:
    new_list.append(i)
print("new list, old way = ", new_list)

new_list = []
new_list = [i for i in my_list]
print("new list, new way = ", new_list)

# Compound list comprehension
my_list = [4, 6, 9, 10]

new_list = [i for i in my_list if i%2 == 0]
print("list comprehension with condition = ", new_list)

new_list = [i**2 for i in my_list if i%2 == 0]
print("expression list comprehension = ", new_list)

new_list = [i**2 if i%2 == 0 else pow(i-1, 2) for i in my_list]
print("compound list comprehension = ", new_list)

listOfWords = ["this","is","a","list","of","words"]
items = [ word[0] for word in listOfWords ]
print("first character of the list words = ", items)

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print("".join(numbers))


"""
Is list comprehension faster?
"""
import time

start = time.time()
[n**2 for n in range(1000000) if n%2==0]
end = time.time()
print(end - start)

def power_two(numbers):
    for n in range(numbers):
        if n%2==0:
            new_list.append(n**2)
    return new_list

start = time.time()
power_two(1000000)
end = time.time()
print(end - start)