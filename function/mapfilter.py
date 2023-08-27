'''
map works on the all elements of iterable/sequence
lets perform square of number without map
'''
# listx=[1,2,3,4]
# for i in listx:
#     i=i**2
#     print(i)

# #out put: 1,4,9,16
# listx=[1,2,3,4]
# listy=[]
# for i in listx:
#     i=i**2
#     listy.append(i)
# print(listy)                #[1, 4, 9, 16]

# map() will take the 2 arguments function and sequence


# listz=[1,2,3,4]

# def mapsquare(n):
#     return n**2

# map(mapsquare,listz)
# print(listz)            #[1, 2, 3, 4]


# listz=[1,2,3,4]

# def mapsquare(n):
#     return n**2

# x=map(mapsquare,listz)
# print(x)                    # <map object at 0x0000022EAEB1AAA0>

# map retursn the object its memory address 

listz=[1,2,3,4]

def mapsquare(n):
    return n**2

x=map(mapsquare,listz)
print(list(x))              # [1, 4, 9, 16] , it is required to convert in to return type , since values are in list so

print(tuple(x))             #empty

listp=(1,2,3,4)
def tupsquare(x):
    return x**2

y=map(tupsquare,listp)
print(tuple(y))             #(1, 4, 9, 16)


listp={1,2,3,4}
def setsquare(x):
    return x**2

y=map(setsquare,listp)
print(set(y))               #{16, 1, 4, 9}  

'''
how to use map & lambada
'''
listm=[1,2,3,4]
m=map(lambda q:q**2,listm)      
print(m)                    #<map object at 0x0000022DFDAEBDF0>
print(list(m))              #[1, 4, 9, 16]

print(list(map(lambda q:q**2,listm)))       #[1, 4, 9, 16]      efficient way of writing the code
print(listm)                #[1, 2, 3, 4]
temp=list(map(lambda q:q**2,listm))
print(f"the value of {temp}")                 #[1, 4, 9, 16]
print(f"the value of listm is {listm}")        #the value of listm is [1, 2, 3, 4]
