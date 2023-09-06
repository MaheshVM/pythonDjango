'''

one error can have multiple exceptions
singe try can have multiple exceptions
it is not prefered way to handle this way, because we get ladder of except statements
so in next we try with another method called preferred way
'''
a=eval(input("enter a first value1: "))
b=eval(input("enter a second value: "))
try:
    print(a/b)
    print(c)                                
except ZeroDivisionError:
    print("an exception is because of zero division raised") 
except NameError:
    print("exception raised due to name not declared")        

print("continued with other list of code")

# enter a first value1: 4
# enter a second value: 2
# 2.0
# exception raised due to name not declared
# continued with other list of code

# enter a first value1: 6
# enter a second value: 0
# an exception is because of zero division raised
# continued with other list of code

