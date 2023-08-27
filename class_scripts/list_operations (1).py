# Add,Modify,Delete - operations. and if you are able to do that, then that DT is a mutable (change) object.
listx=[1,2,3,4,5,12,14]

listx.append(25)
print(listx)

listx.extend([22,32])
print(listx)

print(listx.pop(3)) #LIFO
print(listx) # [1, 2, 3, 5, 12, 14, 25, 22, 32]
# List is mutable type of an object
listx.insert(3,6)
print(listx)


print(listx.index(12))


# deep copy vs shallow copy
print("=================")
listx=[1,2,3,4]
listy=listx # same copy --> [1,2,3,4]  --> deep copy
listz=listx.copy()

print("before any mods to the listx")
print(listx) # [1,2,3,4]
print(listy) # [1,2,3,4]
print(listz) # [1,2,3,4]

listx.append(10)

print("after the  mods to the listx")
print(listx)   # [1,2,3,4,10]
print(listy)   # [1,2,3,4,10]
print(listz)   # [1,2,3,4]


