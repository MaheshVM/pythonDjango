class Person():
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
    def display(self):
        print(self.name+self.addr)

# ob=Person("mahesh","mahendra")
# ob.display()

class child(Person):
    def __init__(self,name,addr):
        super().__init__(name,addr)
        self.year=2020
    def welcome(self):
        print("welcome by",self.name,self.addr,"for the year",self.year)
          

c1=child("mahesh","mahendra")
c1.welcome()       # welcome by mahesh mahendra for the year 2020 