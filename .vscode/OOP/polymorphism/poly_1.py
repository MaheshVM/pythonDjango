'''
below is overlaoding concept
'''
class duck:
    def quack(self):
        print("in first quck slow")

class malar:
    def quack(self):
        print("In second quck loudly")

class eagle:
    def fly():
        print("It can fly")

class makeitquack:
    def __init__(self, bird):           #bird=duck()
        bird.quack()                    #duck.quck()

m=makeitquack(duck())             #passing as a variable to function
m1=makeitquack(malar())           #passing variable as class to the function

# in first quck slow
# In second quck loudly
