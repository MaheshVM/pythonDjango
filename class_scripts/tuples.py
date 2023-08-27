# List is a collection of heterogenous DT which is ordered and changeable(mutablity). Also allows duplicate members. Dynamic data - List
# Tuples is a collection of heterogenous DT which is ordered and unchangeable(immutable). Also allows duplicate members. Static data - Tuple
# tuple =()
# tuple()

tupleg=(1,2,3,4,5,6,5,4,2)
print(type(tupleg))
print(tupleg)
print(tupleg[1:4])

numbers=1,2 # interpreter treats this as tuple of 2 element.
print(numbers) 
print(type(numbers))

numbers=1, # interpreter treats this as tuple of 1 element. (1,)
print(numbers) 
print(type(numbers))

names='Ankit',
print(type(names))

x = 5  
a,b,c = 2,3,4 # unpacking of variables from a tuple. interpreter will treat it as (a,b,c)=(2,3,4)
print(a)
print(b)
print(c)



