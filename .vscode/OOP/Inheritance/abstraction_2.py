'''
abstraction is nothing but hiding the implementation details

class classname:
    pass
there are rules of abstraction
4 rules
1. define a function inside class that we can not implement that method
2. inherit from the abstract class ABC
'''
from abc import ABC,abstractclassmethod

class Shape(ABC):           #rule 1 must inherited from class ABC
    @abstractclassmethod        # add the decorator rule 2
    def area(self):         #can not implement "ATLEAST" one method- rule 3 this is called abstract method
        pass                    #
#s=Shape()                       #TypeError: Can't instantiate abstract class Shape with abstract method area, because of decorator
# rule 4 can not instantiate an abstract class
#the moment we remove decorator abstractmethid we can able to crearte object
#we have to implement this above method in inherited class

class triangle(Shape):
    def area(self,b,h):     # look at this how we implemented function declared in base class and defined in derived class
        res=0.5*b*h
        return res
    
t=triangle()
r=t.area(2,3)
print("area of triangle is",r)
