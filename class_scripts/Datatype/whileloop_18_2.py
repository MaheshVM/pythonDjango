'''
try to avoid using while loop, because may go in infinite loop
may go in infinite loop
while loop we keep executing the statements "as long as the condition is true

syntax:
    while expressio:
        statements of code
major difference between for loop and while is that at point of time for loop get out and exit.
but while go infinite loop from line 22 24 line program
may be better than for
'''
# count=0
# while count < 5:
#     print(count)        # this goes in infinite loop


# count=0
# while count < 5:
#     print(count)            #0 1 2 3 4
#     count+=1 

# listx=[1,2,3,4]
# while listx[3] <= 4:
#     print(listx)

# listx=[1,2,3,4]
# while listx[3] <= 4:
#     print(listx)

# i=1
# while i <6:
#     print(i)
#     i+=1

'''
pass is some thing just line of code some time after loop statement
no any statement there u can write pass
'''
# i=1
# while i < 5:
#     pass              it is just a line of code
# print("continue here")

x=input("enter value:")
if x < 18:
    print("not adult")
print("adult")