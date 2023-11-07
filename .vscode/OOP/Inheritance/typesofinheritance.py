'''
different forms of inheritance

1. single inheritance- when child class inherits from only one parent class
2. multiple inheritance- child class inherits from multiple parent class
unlike c++ and java, python supports multiple inheritance. we can specify all the parents
using coma separated.
'''

class Parent1:
    def __init__(self):
        self.str1="Hello"
        print("Parent1 class")

class Parent2:
    def __init__(self):
        self.str2="Hi"
        print("Parent2 class")

class Parent3:
    pass

class Child(Parent1,Parent2):
    def __init__(self):
         Parent1.__init__(self)
         Parent2.__init__(self)
         print("Child class")

    def display(self):
        print(self.str1+self.str2)


c1=Child()
c1.display()

# Parent1 class
# Parent2 class
# Child class
# HelloHi
    
