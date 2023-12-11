class Person:
  
    def __init__(self,name,addr):
        self.name=name
        self.__addr=addr                #this becomes private to the class Person , so any method within this class can access

    def adding(self):
        return self.name+self.__addr
    
    def __method(self):
        print("Trying to declare private method")
    
p=Person("mahesh","mahendra")
print(p.adding())  

p.__method()            #AttributeError: 'Person' object has no attribute '__method'

#we get the error here since method becomes the private so we can not access it
