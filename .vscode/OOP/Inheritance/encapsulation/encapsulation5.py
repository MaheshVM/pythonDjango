#Data mangling in python- basically to access private variable and method outside the class

#this is left for developer discussion, must used carefully

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

#===Data Mangling==========
print(p._Person__y)                 # 20
# look at this as we can accessing the private variable outside the class here    

p._Person__method()         #  Trying to declare private method

# see we could able to access both private and variable and method using above technique

