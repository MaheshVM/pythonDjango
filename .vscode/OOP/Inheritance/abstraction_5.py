'''
abstraction is nothing but hiding the implementation

define a method/function that can not be implemented in base class
1. inherit from ABC class

Rule 1: inherit from the abstract class ABC
must follow the rules

create abstract method for all the class, its kind of layout for the design architect
'''

from abc import ABC, abstractmethod        # must import from abc


class Shape(ABC):           # rule 1: any class must inherit from ABC class
    @abstractmethod         # rule 2: add the decorator 
    def area(self):
        pass                # rule 3: can not implement this, we can have multiple also  abstract method

#ob=Shape()                  # TypeError: Can't instantiate abstract class Shape with abstract method area
                            # rule 4: can not instantiate an abstract class, means we can not create object of this
                            # its BA to convert in to the class
#rule 5: we can not leave it like open, we have to use it

class Triangle(Shape):      # now if inherited from Shape, its mandatory to implement method what we declared in class "area"
    def area(self,b,h):     # rule 6: its mandatory to implement
        res=0.5*b*h
        return res

t=Triangle()
r=t.area(2,4)
print("area of triangle is",r)      #area of triangle is 4.0

#def area1(self,b,h): if if didnt specify or used abstract method you will end up with error here, 
#TypeError: Can't instantiate abstract class Triangle with abstract method area