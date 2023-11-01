
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
        Person.__init__(self,name,addr)

c1=child("mahesh","mahendra")
c1.display()