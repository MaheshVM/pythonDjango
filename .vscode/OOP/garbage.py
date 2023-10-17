'''
destructor method:
            __del__(self):
'''

import gc
print(gc.isenabled())       #always enabled "true"

#gc.disable()             # how we disable but not to do 

# x=10                      # x is the oject ref to an object of class list
# print(x)
# del x                     # intenally calling __del__ destructor for the class int x created internally
# print(x)                #since it is deleted, NameError: name 'x' is not defined

listx=[1,2,3,4]
print(listx)
del listx
#print(listx)            #NameError: name 'listx' is not defined. Did you mean: 'list'?

#del listx,x             # we can give it like this

class Testgc():
    def __init__(self):
        print("object is created")
    def __del__(self):                  #called at the end of the program, explicitly mentioned in the class so.
        print("deleted the object")

t=Testgc()

# object is created
# deleted the object
y=6
print(y)

    # object is created
    # 6
    # deleted the object
#del t                   # explicitly mentioning to call del function, but not good  practice
# this will overrides __del__method.
#override meaning: already exist and over. if there is __del__ means it will call first this method.
#is same name method and signature is available and overides the existing with previous