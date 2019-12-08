# Variable modifiers: https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python
"""
There are three types of access modifiers in Python: public, private, and protected.
1) Variables with the public access modifiers can be accessed anywhere inside or outside the class.
2) the private variables can only be accessed inside the class.
3) while protected variables can be accessed within the same package.
"""
# Introduction to OOP using Python: https://www.programiz.com/python-programming/object-oriented-programming
"""
One of the popular approach to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:
1) attributes
2) behavior

Let's take an example:

Parrot is an object,
1)) name, age, color are attributes
2) singing, dancing are behavior

This concept is also known as DRY (Don't Repeat Yourself).
"""

"""
In Python, the concept of OOP follows some basic principles:

1) Inheritance	 - A process of using details from a new class without modifying existing class.
2) Encapsulation - Hiding the private details of a class from other objects.
3) Polymorphism	 - A concept of using common operation in different ways for different data input.
"""

# Classes and class attributes
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instance and instance attributes
blu = Parrot("Blu", 10) # instantiate the Parrot class
woo = Parrot("Woo", 15) # instantiate the Parrot class

# access the class attributes
print("Blu is a {}".format(blu.species)) # print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.species)) # print("Woo is also a {}".format(woo.__class__.species))
# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

# Binding and method invocation
class Parrot:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

blu = Parrot("Blu", 10) # instantiate the object
print(blu.sing("'Happy'")) # call our instance methods
print(blu.dance())

# Composition, sub-classes and derivation: https://realpython.com/inheritance-composition-python/#composition-in-python

# Inheritance: https://www.programiz.com/python-programming/object-oriented-programming
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


    # child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

# Built-in functions for classes, instances and other objects

# Plymorphism: https://www.programiz.com/python-programming/object-oriented-programming
"""
Polymorphism is an ability (in OOP) to use common interface for multiple form (data types).
Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). 
However we could use same method to color any shape. This concept is called Polymorphism.
"""

class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()

# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

# Privacy and delegation: https://www.programiz.com/python-programming/object-oriented-programming
"""
Using OOP in Python, we can restrict access to methods and variables. 
This prevent data from direct modification which is called encapsulation. 
In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.
"""
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000 # change the price
c.sell()

c.setMaxPrice(1000) # using setter function
c.sell()

# Overview of built-in python classes and modules
"""
Python has two built-in functions that work with inheritance:
Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. 
However, issubclass(float, int) is False since float is not a subclass of int.
"""
print(isinstance(c, Computer))

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

print(issubclass(MappingSubclass, Mapping))

Built-in functions for modules: https://www.tutorialsteacher.com/python/python-builtin-modules