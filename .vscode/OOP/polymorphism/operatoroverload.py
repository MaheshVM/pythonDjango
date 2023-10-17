# a=2
# b=3
# print(a+b)

# print(a.__add__(b))         #5 executed internally like a+b __add__ built in function available 
#                             #__add__(self,other)


class overload:
    def __init__(self,a):
        self.a=a

    def __add__(self,ob1):
        self.a=self.a+ob1.a
    def disp(self):
        print("in class",self.a)
    
o1=overload(2)
o2=overload(5)
o1+o2
o1.disp()
