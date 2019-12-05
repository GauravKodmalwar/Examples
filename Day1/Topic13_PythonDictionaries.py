#Python dictionaries
"""
Dictionary in Python is an unordered collection of data values, used to store data values like a map,
which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair.
Key value is provided in the dictionary to make it more optimized.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print("How to get the values from dictionary: ", thisdict.get("model"))

# updating values in dictionary
thisdict["year"] = 2018
print(thisdict.get("year"))

print("Printing all the values in the dictionary")
for x in thisdict:
  print(x)
  print("===> ", thisdict.get(x))

for x, y in thisdict.items():
  print("key is {} and value is {}".format(x, y))

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Adding new value in the dictionary
thisdict["color"] = "red"
print(thisdict)

temp = thisdict.pop("model")
print(temp)
print(thisdict)

# Explore few more functions yourself like popitem, copy, clear, dict(name=value, name=value), update, values, keys