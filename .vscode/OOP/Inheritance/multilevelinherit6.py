#multilevel

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass
'''
any level broken could not access
'''


class A():
    def a(self):
        print("AAA")

class B(A):
    def b(self):
        print("BBB")

class C(B):
    def c(self):
        print("CCC")

class D(C):
    def d(self):
        print("DDD")

ob=D()
ob.a()                  #AAA calls A class a function
# ob.b()                  #BBB
# ob.c()                  #CCC
# ob.d()                  #DDD
#D->C->B->A->object
print(issubclass(D,C))      #True   to check subclass
print(isinstance(D,D))      #False
print(isinstance(ob,D))     #True
print(isinstance(ob,A))     #True is kind of (d,(A,B,C,D))

x=5
print(isinstance(x,int))        #True   as x is class of int