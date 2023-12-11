class Person:
    x=10
    __y=20
    def __init__(self,name,addr):
        self.name=name
        self.__addr=addr                #this becomes private to the class Person , so any method within this class can access

    def adding(self):
        return self.name+self.__addr
    
    def __method(self):
        print("Trying to declare private method")
    
p=Person("mahesh","mahendra")
print(p.adding())  
print(p.x)
print(p.__y)            # here we get the error since private variable trying to access it outside the class

#AttributeError: 'Person' object has no attribute '__y'
