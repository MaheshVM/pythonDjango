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
    
ob1=Name("mahesh")
ob2=Name("Mahendra")
ob3=Name("Belgaum")
print(ob1+ob2+ob3)          #maheshMahendraBelgaum
#ob1=ob1+ob2+ob3
#ob1.disp()          #maheshMahendraBelgaum