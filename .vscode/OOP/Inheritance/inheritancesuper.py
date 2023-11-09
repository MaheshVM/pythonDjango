class Employee():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Hr(Employee):
    def __init__(self,hname,hage,id,category):
        super().__init__(hname,hage)
        # self.hname=hname
        # self.hage=hage
        self.id=id
        self.category=category
    
    def display(self):
        print("HR name",self.name)
        print("HR age",self.age)
        print("HR id",self.id)
        print("HR category",self.category)
class software(Employee):
    def __init__(self,sname,sage,projectname,tech):
        super().__init__(sname,sage)
        # self.sname=sname
        # self.sage=sage
        self.projectname=projectname
        self.tech=tech

    def display(self):
        print("Software name",self.name)
        print("Software age",self.age)
        print("software id",self.projectname)
        print("software category",self.tech)

h1=Hr("mahesh",45,1234,"admin")
s1=software("vijay",44,"devop","docker")
h1.display()
s1.display()

# HR name mahesh
# HR age 45
# HR id 1234
# HR category admin
# Software name vijay
# Software age 44
# software id devop
# software category docker
