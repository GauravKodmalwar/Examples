# Using re module
import re
txt = "The rain in Spain"

# Searching with Regular Expression
x = re.search("^The.*Spain$", txt)
print(x.start())
print(x.end())

# Replacing with Regular Expression

# Reusing Regular Expression with re.compile
p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark")) # findall() searches for the Regular Expression and return a list upon finding

p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# Match function ==> this function returns the text
x = re.match("^The.*Spain$", txt)
print("matched string is ==> {}".format(x.group()))

# Search function

# Regular expression patterns: https://www.w3schools.com/python/python_regex.asp#search

# Backreferences: https://stackoverflow.com/questions/47719562/using-python-regex-with-backreference-matches

# Translations

# Finding pin code
NameAge ="""
Kiran is 45 and Rashmi is 24
Rohan is 56 and Surya is 76
"""
ages = re.findall(r'\d[0-9]', NameAge)
names = re.findall(r'\b[A-Z][a-z]*', NameAge)

ageDict = {}
x = 0

for name in names:
    ageDict[name] = ages[x]
    x += 1

print("Name and age values are {}".format(ageDict))

# Finding valid email ID. Handling backspaces.
text = """
akshay@xyz.com
dfd-2.com
dfadscom
acd@dxc.com
"""
temp = re.compile("\n")
print("Entire text in one line {}".format(temp.sub(" ", text)))

# Finding phone number of a particular country
phoneNumbers = """
456-134-2567
245-764-1938
456-198-2956
356-15b-3677
"""
print("valid phone numbers are here: ".format(re.findall('\d{2}-\d{3}-\d{3}', phoneNumbers)))