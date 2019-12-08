# Right click on folder and select Mark directory as Source root ===> to avoid unresolved references

# Modules basics
"""
Simply, a module is a file consisting of Python code (code library).
A module can define functions, classes and variables. A module can also include runnable code.
"""
import BasicModule
BasicModule.greeting(name="Pythoner")
print(BasicModule.person1["age"])
print(BasicModule.person1.get("age"))

import BasicModule as bs # Import as
a = bs.person1["age"]
print(a)

from BasicModule import person1 # Import From Module
print(person1["age"])

# Packages
"""
Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.
Each package in Python is a directory which MUST contain a special file called __init__.py. 
This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.
If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. 
We also must not forget to add the __init__.py file inside the foo directory.
"""

# Package creation and importing: https://www.w3schools.com/python/python_modules.asp
# https://www.learnpython.org/en/Modules_and_Packages
from pingpong import draw
draw.draw_game()

from pingpong import play
play.pause()

from pingpong.draw import *
from pingpong.play import *
draw_game()
pause()

"""dir command returns list of the attributes and methods of any object"""
print(dir("BasicModule"))

# Using __all__ and _ variables: https://www.geeksforgeeks.org/underscore-_-python/
"""
__all__ doesn't restrict access to functions or attributes but it provides flexibility to provide access to public level attributes/function.
Whenever you use "import *" then all with public access (by default its public in Python) or all with __all__ given access to calling function
"""

from pingpong.exampeof__all__ import *

print(bar)
print(baz)

#print(waz) # The following will trigger an exception, as "waz" is not exported by the module

"""
_ i.e. single under score is for ignoring, i.e. user is not interested in values.
"""
for _ in range(3):
    print("Test")

"""
Python has their by default keywords which we can not use as the variable name. 
To avoid such conflict between python keyword and variable we use underscore after name.
"""
from pingpong.underscore_example import my_defination
my_defination()

"""
_ i.e. single under score before a function or variable means those are internal and can be modified using class ONLY. Also called "non-public".
"""
from pingpong.underscore_example import *
test = Prefix()
print(test.public)
print(test._private) # weak Private

public_api()
#_private_api() # This will throw an error as its private function

"""
__ i.e. double under score means, those functions or attributes are private. Those can be overloaded but not be created. 
In Python, you can still access the attributes even if they are private by their internal functions.
"""
from pingpong.underscore_example import *
obj = Myclass()
# print(obj.__variable) # this will throw error
obj.func()

"""
Name with start with __ and ends with same considers special methods in Python. 
Python provide this methods to use it as the operator overloading depending on the user.
Python provides this convention to differentiate between the user defined function with the module’s function
"""
obj.__print__(5, 10)

"""
Since there is no main() function in Python, when the command to run a python program is given to the interpreter, 
the code that is at level 0 indentation is to be executed. However, before doing that, it will define a few special variables.
 __name__ is one such special variable. If the source file is executed as the main program, the interpreter sets the __name__ variable to have a 
 value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.
"""
print(__name__)

# Using thirdparty modules or packages
import time
from time import asctime
asctime()
