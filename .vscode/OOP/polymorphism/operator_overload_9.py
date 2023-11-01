class Name:
    def __init__(self,name):
        self.name=name
      
    
    def __add__(self,o1):
        fname=self.name+o1.name
        return Name(fname)
        
    def __str__(self):
        return self.name

    def disp(self):
        print(self.name)

s1=Name("abc")
s2=Name("abc")
if s1==s2:
    print("they are equal") 
else:
    print("they are not equal")

#they are not equal
print(id(s1))           #2007752893456
print(id(s2))           #2007752893840
# on every run it will change
# 2088693589008
# 2088693589392

#these are not memory address it is identity of the object number, human readable format number
