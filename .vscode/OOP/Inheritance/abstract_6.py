from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):             # if we mention the parameter also no point in declare it
        pass

class snake(Animal):
    def move(self):
        print("I can crawl")

class cat(Animal):
    def move(self):
        print("I can meuu")

class dog(Animal):
    def move(self):
        print("I can bark")

s=snake()
s.move()

c=cat()
c.move()

d=dog()
d.move()

# I can crawl
# I can meuu
# I can bark
