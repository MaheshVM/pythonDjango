# List is a collection of heterogenous DT which is ordered and changeable(mutablity). Also allows duplicate members. Dynamic data - List
# Tuples is a collection of heterogenous DT which is ordered and unchangeable(immutable). Also allows duplicate members. Static data - Tuple
# Set is a collection of heterogenous DT which is "unordered" and changeable(mutable). Also does NOT allows duplicate members. They do not follow indexing as they save based on hash mechanism. They are non-subscriptable(indexing)
# set= {1,2,3}  there is no way to create an empty set using ={} becoz thats an empty dict.
# set()

seteg={1,2,3,4,'ankit',4,3,2,1,3,4,5} # 
print(type(seteg)) 
print(seteg)

print("========")
set1={1,2,3,4,5}
set2={5,6,7}

print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set2.difference(set1))
print(set2 - set1)

set1={1,2,3}
set1.add(4)
print(set1)

set1.pop()
print(set1)

set1.update({4,5,6})
print(set1)


oldset={1,4,5,6}
newset=oldset.add(10)
print(newset) # {1,4,5,6,10}....error.....None


oldset.discard(4)
print(oldset)


newset=frozenset(oldset) # converts the oldset (which was mutable) into immutable object(cannot add, modify or delete)

