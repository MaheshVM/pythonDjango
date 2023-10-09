'''
3 ways to define class
1. class Class_Naame:       ex: class Emploee:
2. class Class_Name():      ex: class Employee():
3. class Class_Name(object):    ex: class Employee(object):, internally called object class
'''

class First:
    ''' This is a doc string for class'''
    def __init__(self):
        print("First statement of the object")
    def show(self):
        print("This is first class")

# steps to create
#1
First()             #"First statement of the object"
#2 create a reference  ref_var=className()
x=First()       # object  is created kind of First, and referencing to x variable
#this also prints "First statement of the object"
x.show()
# This is first class
print(First.__doc__)        # this will prints the above doc string ""
#This is a doc string for class