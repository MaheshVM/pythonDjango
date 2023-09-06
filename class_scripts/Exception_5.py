'''
prefered  method of exception handling
below is the optimized way of writing the exception
'''
# a=10
# b=3
# try:
#     print(a/b)
#     print(c)
# except (ZeroDivisionError,NameError) as e_msg:  #e_msg can be anything you like name can be given
#     print("AN exception was raised by",e_msg)

# print("AFter block of Exception")

# for above we get:
#     3.3333333333333335
# AN exception was raised by name 'c' is not defined
# AFter block of Exception

# a=10
# b=0
# try:
#     print(a/b)
#     print(c)
# except (ZeroDivisionError,NameError) as e_msg:  #e_msg can be anything you like name can be given
#     print("AN exception was raised by",e_msg)   # here e_msg will get the message raised by exception and prints as seen

# print("AFter block of Exception")

#AN exception was raised by division by zero
# AFter block of Exception


'''-------------------------------------------'''
# a=10
# b=0
# try:
#     print(a/b)
#     print(c)
# except Exception as e_msg:                      #here universal exception has been declared so that will take accordingly
#     print("AN exception was raised by",e_msg)   # Exception is mother of all the exception

# print("AFter block of Exception")

# AN exception was raised by division by zero
# AFter block of Exception

#above can be kepr as default way of exception to handle the situation
# a=10
# b=0
# try:
#     print(a/b)
#     print(c)                                # here c is not assigned any value it is an error how did handled 
# except(ZeroDivisionError,NameError):         #if it could not captured then default exception will definetly catch the exception
#     print("an exception is raised")
# except Exception as e_msg:
#     print("Universal way of giving answer")

# print("after the block code" )

# a=10
# b=4
# try:
#     print(a/b)
#     print(c)                                # here c is not assigned any value it is an error how did handled 
# except(ZeroDivisionError) as e_msg:         
#     print("an exception is raised",e_msg)
# except Exception as e_msg:
#     print("Universal way of giving answer",e_msg)     #in this this will catch so that if above except did not at leat parent exception will catch it

# print("after the block code" )

# 2.5
# Universal way of giving answer name 'c' is not defined
# after the block code
# try to keep Exception in last because its mother of all so


a=10
b=4
try:
    print(a/b)
    #print(c)                                # here c is not assigned any value it is an error how did handled 
except(ZeroDivisionError) as e_msg:         
    print("an exception is raised",e_msg)
else: 
    print("i am in else block")     #in this this will catch so that if above except did not at leat parent exception will catch it
finally:
    print("final code")


print("after the block code" )

# output:
# 2.5
# i am in else block
# final code
# after the block code


