#list operations: add, modify,delete. so it is mutable(change)
#since list is mutable

listx=[1,2,3,4,5,6,7]
listx.append(18)            #here it is updated, no issues
print(listx)
print(listx.append(20))         #prints None because oeprational output is none. None
#listx.extend(50,60)             #this is not correct
listx.extend([50,60])
print(listx)                #[1, 2, 3, 4, 5, 6, 7, 18, 20, 50, 60]      
print(listx.pop())          # 60 LIFO, by default last element
print(listx.pop(2))         # 3

#append & extend works always to append at the end
#if wanted to add in between use insert
listx.insert(2,77)          #[1, 2, 77, 4, 5, 6, 7, 18, 20, 50]  insert(indexpos, value)
print(listx)

print(listx.index(5))           #give the position (index in the ) list , 4

#deep copy vs shallow copy
print("-------------------------------------------")
listy=[1,2,3,4]      #same copy [1,2,3]---> deep copy
listz=listy             #means listy & listz point to the same location whatever changes we do one will affect other also 
listp=listy.copy()      #separate copy with bit by bit copy , shallow copy

print(listy)       # [1, 2, 3, 4]          
print(listz)       # [1, 2, 3, 4]
print(listp)       # [1, 2, 3, 4]

listy.append(10)
print(listy)       # [1, 2, 3, 4, 10]     
print(listz)       # [1, 2, 3, 4, 10]
print(listp)       # [1, 2, 3, 4]