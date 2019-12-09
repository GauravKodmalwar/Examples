# https://www.geeksforgeeks.org/working-with-json-data-in-python/

import json

# {key:value mapping}
a = {"name": "John",
     "age": 31,
     "Salary": 25000}

b = json.dumps(a) # conversion to JSON done by dumps() function
print(b) # printing the output

# JSON supports dumps for all types of data
import json

print(json.dumps(['Welcome', "to", "GeeksforGeeks"]))
print(json.dumps(("Welcome", "to", "GeeksforGeeks")))
print(json.dumps("Hi"))
print(json.dumps(123))
print(json.dumps(23.572))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Serialization example
var = {
      "Subjects": {
                  "Maths":85,
                  "Physics":90
                   }
      }

with open("Sample.json", "w") as p:
    p.write(json.dumps(var))

# Deserializing JSON
with open("Sample.json", "r") as read_it:
    data = json.load(read_it)

print(data)