'''
is a multiple exception
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