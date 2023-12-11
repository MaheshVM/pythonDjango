from abc import ABC, abstractmethod

class Parent(ABC):
    x=100
    @abstractmethod
    def  method1(self):
        print("parent abstract method")


class child(Parent):
    def method1(self):
        print("Child class")
        super().method1()           # but it should not be 
        print(super().x)            # give the : 100

c=child()
c.method1()

# Child class
# parent abstract method