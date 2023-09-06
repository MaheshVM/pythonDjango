a=eval(input("enter a first value1: "))
b=eval(input("enter a second value: "))
try:
    print(a/b)
    print(c)                                # here c is not assigned any value it is an error how did handled 
except(ZeroDivisionError,NameError):
    print("an exception is raised")         

print("continued with other list of code")

'''
in above code we dont know from the error is either line 4 or 5
in above it may happens that we get Nameerror
we can handle with multiple error exc eptions
one error can have multiple exceptions

'''