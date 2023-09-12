'''
instead of self can give any name, mahesh or abc, pqr or anything
good practice give key word "self" only
'''
class Person:
    ''' Details of employee'''
    name="mahesh"
    city="pune"
    code=123

    #def speak():   without self gives the error,implicitly it will not called so error
    def speak(self):
        print("can speak english")
    #def write(): implicitly it will not called so error
    def write(self):
        print("can write english and kannda")

ob1=Person()
print(Person.name)
print(Person.city)
print(Person.code)

#ob1.speak()     #gives error
#TypeError: Person.speak() takes 0 positional arguments but 1 was given
#as implicitly passing the object Person()
# so give with "self" in the functions
ob1.speak()         #can speak english
ob1.write()         #can write english and kannda
print(ob1.__doc__)  # Details of employee
#__doc__ is inbuilt functions
