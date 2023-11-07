class Person():
    def __init__(self):
        pass
    
    def temp(self):
        print("parent class")

class child(Person):
    def temp(self):
        super()
        print("in child class")


c1=child()
c1.temp()
