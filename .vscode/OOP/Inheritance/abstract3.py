from abc import ABC, abstractclassmethod

class animal():

    @abstractclassmethod
    def move(self):
        pass

class snake(animal):

    def move(self):
        print("pisss")
    
class dog(animal):

    def move(self):
        print("bark")

class cat(animal):
    def move(self):
        print("mmmioo")


s=snake()
s.move()
d=dog()
d.move()
c=cat()
c.move()

# pisss
# bark
# mmmioo




    