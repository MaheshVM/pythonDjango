'''
definition of function always before the call.in editor also at the begining before call.


Modules: is nothing but functions written inside a class

Types of functions:
1. in built functions- ex: print, type, all defined by python
2. user defined functions or programmer functions
3. lambda functions- efficient  and big line of codes written in few lines of code
4. magic methods/dundle methods or super methods- they are inside the class ex: __ad__..

Syntax :
    def <functionName>(param1, param2...):
        block of statements
functions must be defined before the call, may be at the beginning only have to declare it
until function call it will not be loaded
return statement is optional in python
return <value> or expression or even a string
in python all functions by default return None

firstclass objects:
1. assign functions to variables
2. assigning functions to another functions
3. functions can be apssed as a parameter to another function
'''
# def add_two_nos(a,b):
#     print(a+b)
#     # return <value> or expression or print statements


#add_two_nos(5,6)

def add_two_nos(a,b):
#     print(a+b)
      return a+b

# def add_two_nos(a,b):
# # #     print(a+b)
#        return "the sum of two numbers:",a, "and",b, "is", a+b
# # print(add_two_nos(7,8))
# print(add_two_nos(50,100))
# print(add_two_nos(3.5,4.2))
# print(add_two_nos("hi","hello"))
a=10
b=10
print(add_two_nos(a,b))
a=30
b=40
print(add_two_nos(a,b))
print(a)
print(b)
a=100
b=100
print(add_two_nos(a,b))
print(a,b)

def mul(a,b):
      return a*b

y=mul(5,6)
print(y)            #30