''''
Hierarchy
parent1->child1
         child2
         child3

Hybrid
python supports all forms of inheritance
    it is kind of multi level and multiple combination

Cyclic: conceptual, any class that is inheriting by itself. no life scenario and no programming support
less used

super
MRO
diamond access problem
'''

class Employee():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Hr(Employee):
    def __init__(self,hname,hage,id,category):
        self.hname=hname
        self.hage=hage
        self.id=id
        self.category=category
    
    def display(self):
        print("HR name",self.hname)
        print("HR age",self.hage)
        print("HR id",self.id)
        print("HR category",self.category)
class software(Employee):
    def __init__(self,sname,sage,projectname,tech):
        self.sname=sname
        self.sage=sage
        self.projectname=projectname
        self.tech=tech

    def display(self):
        print("Software name",self.sname)
        print("Software age",self.sage)
        print("software id",self.projectname)
        print("software category",self.tech)

h1=Hr("mahesh",45,1234,"admin")
s1=software("vijay",44,"devop","docker")
h1.display()
s1.display()
