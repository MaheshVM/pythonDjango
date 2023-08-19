'''clearWhat is tuple

List is a collection of heterogeneous data type which is ordered and changeable(mutability)
also allows duplicate members

Tuple: is a collection of heterogeneous data type which is ordered and unchangeable (immutable).
	also allows duplicate members
we can not change means add. delete and modify. rest other thing indexing slicing all remain same like list
can not change the original tuple.
we dont have add, delete & modify function

syntax :  tuple=()
in built tuple()

use case: if data is more of dynamic then we do use "list"
if data is static then we do use tuple

try to use naming convention
depend on data we do use required to use list/tuple

empty list:
listx=[]    // planed use so we declare it
'''


tupleg=(1,2,3,4,6,5,6,2)
print(type(tupleg)) 
print(tupleg)
print(tupleg[2])        #3
print(tupleg[1:3])      #(2, 3)

num=1,      #treated as single element tuple
nu=1,2      #interpreter treats this as  tuple of 2 element             
print(num)
print(type(num))    #tuple type
print(nu)

a,b,c=1,2,3     # unpacking of variables from tuple. interpretor will treat as 
print(a)        #1
print(b)        #2
print(c)        #3