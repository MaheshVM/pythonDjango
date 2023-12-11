class Person:
    def __init__(self,name,addr):
        self.name=name
        self.__addr=addr                #this becomes private to the class Person , so any method within this class can access

    def adding(self):
        return self.name+self.__addr
    
p=Person("mahesh","mahendra")
print(p.adding())                   #maheshmahendra
         
