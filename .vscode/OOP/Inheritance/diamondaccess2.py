
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

class parent4(parent1):
    def show(self):
        print("parent4 class")
        super().show()


class child(parent2,parent3,parent4):
    def show(self):
        print("child class")
        super().show()

ob=child()
ob.show()
# child class
# parent2 class
print(child.mro())
'''
step1 : c,p2,p1,0,p3,p1,o,p4,p1,o
step2 : c,p2,p3,p4,p1,o     ---MRO for the given class

'''
# child class
# parent2 class 
# parent3 class
# parent4 class
# Parent1 class
# [<class '__main__.child'>, <class '__main__.parent2'>, <class '__main__.parent3'>, <class '__main__.parent4'>, <class '__main__.parent1'>, <class 'object'>]
