'''
function comprehensiove
'''
def getval(n):
    for i in range(n):
        print(i)
        yield

#getval(5)           # we get 01,2,3,4,5
print(type(getval(5)))  #<class 'generator'>, because yield made this functiona generator
next(getval(5))        #0
next(getval(5))        #0
next(getval(5))        #0