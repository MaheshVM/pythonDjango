# import module1,module3
'''
There are many ways to call the module1 function here
note that __pycache__ folder is created here once after the execution
you can right click and get the relative path of the module :class_scripts\modules\module1.py
pyc - python cache
on every execution cache will go on create
observed that on every module new cache is created
any change in the modules it will recreate the cache files, with same name of the cache previous.
'''

# module1.myName("mahesh")        #The name of the person is mahesh
# module3.getCity("Pune")         # the person lives in the city Pune
# print(module1.x)                # 5 of the module1's x variable value
# print(module3.x)                # 10 of the module3's x variable value

print("==========second way to use ===============")
'''
isntead to import whole module we can import only the corresponding function required
not require any . notatin in calling the functions
'''
# from module1 import myName,x          #this imports only the function, on the bases you can add multiple functions as required
# from module3 import getCity
# x=100
# myName("Vijay")                 #The name of the person is Vijay
# getCity("hubli")                #the person lives in the city hubli
# print("the value will be",x)    #100    it refers the local file x
# from module3 import x
# print("the module file x is", x)    #10 from module3's x value

import module1 as m1
import module3 as m3
x=100
m1.myName("Gajanan")            #The name of the person is Gajanan
m3.getCity("Banagalore")        #the person lives in the city Banagalore
print(m1.x)                     # we get thye m1 's x variable x=5
print(m3.x)                     # we get                      
