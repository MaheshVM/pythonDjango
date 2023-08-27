# List is a collection of heterogenous DT which is ordered and changeable(mutablity). Also allows duplicate members. Dynamic data - List
# Tuples is a collection of heterogenous DT which is ordered and unchangeable(immutable). Also allows duplicate members. Static data - Tuple
# Set is a collection of heterogenous DT which is "unordered" and changeable(mutable). Also does NOT allows duplicate members. They do not follow indexing as they save based on hash mechanism. They are non-subscriptable(indexing)
# Dictionary key value pair concept, is a collection of heterogenous DT which is ordered. Also allows duplicate members as Values. Dynamic data
# Dictionary items are present in K:V pairs. [1,2,3], (1,2,3) {1,2,3}, d1={1:2,3:45,50:60}
# keys are immutable objects - numbers, strings,tuple, frozenset. Canot be duplicated.
# values - Dont care,means anything means mutable....- list, sets, tuple,
# dict()

careg={
    "brand":"Audi",
    'model':'q5',
    'year': 2023,
    'variant':'v4',
}

print(careg) # {'brand': 'Audi', 'model': 'q5', 'year': 2023}

print("before")
print(careg["model"])
print("after")
careg['model']='v6'
print(careg['model'])


dict2={
    (1,20):'onetwo',
    'name':"Mahesh",
}
print(dict2[(1,20)])


#a=(1,2,3,4,5,1,2,10,12,13,12,['ankit','Mahesh',"Naveen","Vijay"],89)
a=(1,2,3,4,5,1,2,10,12,13,12,89)
print(a)
print(type(a))
d1={
    a:'This is going to work?',#(1,2,3,4,5,1,2,10,12,13,12,'ankit',89):'This is going to work?'
    'temp': "This is temp",

}

#print(d1[a])


print("======")
soft_emp={
    'emp_id':1234,
    'emp_name':"Naveen",
    'emp_height': 6.5,
    'languages':['English','Hindi','Spanish',['Python','C','C++',"JAVA"]],
    'address':('res','off'),
    'M':True,
    'education':{"UG","PG"},
}

print(soft_emp)
print(soft_emp['languages'])


print(soft_emp.keys()) # dict_keys(['emp_id', 'emp_name', 'emp_height', 'languages', 'address', 'M', 'education'])
print(soft_emp.values()) # dict_values([1234, 'Naveen', 6.5, ['English', 'Hindi', 'Spanish', ['Python', 'C', 'C++', 'JAVA']], ('res', 'off'), True, {'PG', 'UG'}])
print(soft_emp.items())
# dict_items([('emp_id', 1234), ('emp_name', 'Naveen'), ('emp_height', 6.5), ('languages', ['English', 'Hindi', 'Spanish', ['Python', 'C', 'C++', 'JAVA']]), ('address', ('res', 'off')), ('M', True), ('education', {'PG', 'UG'})])

