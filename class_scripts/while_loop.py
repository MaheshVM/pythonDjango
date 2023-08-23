# with while loop we keep executing the statments "as long as the condition is true"
# when using while loop - first think of the condition to get out of the while loop.
# while expression:
#   statements of while code


count=0
while count <  5:
    print(count)
    #count=count+1
    count+=1 # #count=count+1

listx=[1,2,3,4]
""" while listx[3] <=4:
    print(listx) """

i=1
while i < 6:
    print(i)
    #break
    i+=1 # that condtion that i have to think first to get out of the while loop.


# pass - is a reserved keyword that is a developers tool.
while i <6:
    #print(i**2) # customer has not decided yet what he wants to do with this req.
    pass

print("continue with yoour program")