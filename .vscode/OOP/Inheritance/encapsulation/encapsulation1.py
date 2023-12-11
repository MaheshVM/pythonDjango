class Parent:
    def __init__(self):
        self.__a=5      #private instance variable
        #__b=10          #private local variable
        self.c=15

class Child(Parent):
    def __init__(self):
        super().__init__()      #calling the constructor
        print(self.__a)
        print(self.c)


c=Child()           #AttributeError: 'Child' object has no attribute '_Child__a'

'''
since a becomes the private variable to the parent so we can not able to access it
'''