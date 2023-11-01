'''
super() used in child to call parent class methods, is kind of calling object reference
'''

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
        # Person.__init__(self,name,addr)
        super().__init__(name,addr)
        super().display()   

c1=child("mahesh","mahendra")
#c1.display()
#maheshmahendra