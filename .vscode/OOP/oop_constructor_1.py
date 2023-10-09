'''
constructor: object creation & deletion
in built function __init__(self)    already there in any class
it allocates memory to the class.
it creates object also.
this constructor is called when you create object

deletion: for deletion called destructor

syntax:
        __init__(self)      : initializing class
types of constructor
1. default 
2. parametrized constructor
unlike java who have multiple constructor, python will not support that.

say 
def __init__(self):
    pass

def __init__(self, a,b):
    pass

in above matter will call the last one from top to bottom so first will be ignored so.
correspondingly there are in c++

1. default consrucor:
        no parameters, self is implicitly passed
2. parameterized constructor- with more paarmeters with self

there should not be any print statements inside the __init__ function
'''
# class Employee():
#     ''' constructor implementation'''
     #constructor function
#     def __init__(self):
#         print("calling constructor1")
#     def display(self):
#         print("calling normal function")

# p=Employee()
#calling constructor1

# class Employee(object):                 # see how we creatd because all classes parented from "object" class
#     ''' constructor implementation'''
#     #constructor function
#     def __init__(self):
#         print("calling constructor1")
#     def display(self):
#         print("calling normal function")

# p=Employee()
# calling constructor1

'''
constructor overloading but called last one
'''
class Employee(object):                 # see how we creatd because all classes parented from "object" class
    ''' constructor implementation'''
    #constructor function
    def __init__(self):
        print("calling constructor1")
    def __init__(self):
        print("calling constructor2")
    def display(self):
        print("calling normal function")

p=Employee()

output:
calling constructor2



