# tuplex=(1,2,3,4,5)
# print(type(tuplex))
# print()
'''
set is unordered
changeable
we cant create empty set
no duplication of numbers
not follow indexing, non subscripting
in built function set()
concatenation not supported
operations on sets can be similar to set mathematical operations
'''
# setx={1,2,3,4,'Mahesh','vm',1,2,3,4,5,6}
# print(type(setx))
# print(setx)
# set1={1,2,3,4,5}
# set2={5,6,7}
# print(set1.union(set2))
# print(set1 | set2)

# print(set1.intersection(set2))
# print(set1 & set2)

# print(set1.difference(set2))        #what is there in set1 not in set2
# print(set1-set2)                    # same as previous

# set3={1,2,3,4}
# set3.add(5)
# print(set3)                     #{1, 2, 3, 4, 5}

# set3.pop()
# print(set3)

# print(set3.update({5,6,7}))     #prints None
# print(set3)

old={1,2,3}
new=old.add(10)         #operation will be asigned to new variable so 
print(new)              # we get None
new=old
print(new)              #{10, 1, 2, 3}
old.discard(2)          #take out particular element from the set 2
print(old)              # {10, 1, 3}
test=frozenset(old)     #converts old set mutable to immutable test set
print(test)
