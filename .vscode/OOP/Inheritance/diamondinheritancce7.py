'''
MRO is the solution to the problem

'''

class parent1():
    def show(self):
        print("Parent1 class")

class parent2(parent1):
    def show(self):
        print("parent2 class")
        super().show()
class parent3(parent1):
    def show(self):
        print("parent3 class")
        super().show()
#child class
# parent2 class
# parent3 class
# Parent1 class

'''
since there is no supe().show() so we got the below output
uneless you give the command supe() classes will npt inherited from any base class
'''
class child(parent2,parent3):
    def show(self):
        print("child class")
        super().show()

ob=child()
ob.show()
# child class
# parent2 class
print(child.mro())
#[<class '__main__.child'>, <class '__main__.parent2'>, <class '__main__.parent3'>, <class '__main__.parent1'>, <class 'object'>]

'''
step1 : c,p2,p1,o,p3,p1,0
step2 : c,p2,p3,p1,o
'''