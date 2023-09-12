# yeild it means break the loop
# thin of yield is some thing breaks the line and go back to the calling line
# added recently dictionary comprehension
# yield--> calls internal dundle method named __iter__ and then next()--> dundle method called
# is a kind of pointer
#x=(x for x in str1)    x hold the address
def getval(n):
    #yield                   # it also wont give the value, None
    for i in range(n):
        #yield               #will not get the value, None
        print(i)    
        #yield               # we get 0 , 0, 0 ,0 as if every time will calls from begining we get the same value 0
    yield                   #0,1,2,3,4,

#getval(5)           # we  get 01,2,3,4,5
print(next(getval(5)))      #01234
print(next(getval(5)))      #012334