class complex:
    def __init__(self, a):
        self.a = a
        #self.b = b
 
     # adding two objects
    def __add__(self, other):
        self.a= self.a + other.a
 
Ob1 = complex(1)
Ob2 = complex(2)
ob3=complex(4)
ob4=complex(10)
# ob3 = complex(4,4)
ob1=Ob1+Ob2+ob3
print(ob1)