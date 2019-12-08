# Single underscore
class MyClass():
    def __init__(self):
        print("Initilization OK")

def my_defination(var1=1, class_= MyClass):
        print(var1)
        print(class_)

class Prefix:
    def __init__(self):
        self.public = 10
        self._private = 12

def public_api():
    print("public api")

def _private_api():
    print("private api")

# Double underscore
class Myclass():
    def __init__(self):
        self.__variable = 10

    def func(self):
        print(self.__variable)

    def __print__(self, a, b):
        print(a * b)
        print(__name__)