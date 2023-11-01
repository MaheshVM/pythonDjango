class overload:
    def __init__(self,a):
        self.a=a

    def __add__(self,ob1):
        self.a=self.a+ob1.a
        #tmp=overload(x)
        return self

    def disp(self):
        print("in class",self.a)

o1=overload(3)
o2=overload(4)
o3=overload(7)
o4=overload(10)
o1+o2+o3+o4             
o1.disp()               #in class 24