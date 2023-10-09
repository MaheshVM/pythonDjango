'''
self must be the first argument in methods of class
instead of self anything you can use name "del","mahesh"
'''
class Person:
    Name='mahesh'
    age=40
    city='belgaum'
    def cityfrom(self):             #if it is empty gives error over here, mentioned at least self
        print("my data")

p=Person()
print(p.Name)
print(p.age)
print(p.city)
p.cityfrom()    

# mahesh
# 40
# belgaum
# my data


