class Name:
    def __init__(self,name):
        self.name=name
      
    
    def __add__(self,o1):
        return self.name+o1.name
       # return self
    def disp(self):
        print(self.name)
    
ob1=Name("mahesh")
ob2=Name("Mahendra")
print(ob1+ob2)
#ob1.disp()