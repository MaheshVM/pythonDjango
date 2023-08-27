listx=[(1,'One'),(2,'Two'),(3,'three')]
d1=dict(listx)

print(d1) #{1: 'One', 2: 'Two', 3: 'three'}
print(type(d1))

d1.pop(1)
print(d1)

d1.popitem()
print(d1)

d1.update({1:'one',4:"four"})
print(d1)

d2={5:'five',6:"six"}
d1.update(d2)
print(d1)

# d1={2: 'Two', 1: 'one', 4: 'four', 5: 'five', 6: 'six'}
d3={1:'one',2:"TOOO"}
d1.update(d3)
print(d1)

for x in d1.keys():
    print(x)

for x in d1.values():
    print(x)

for (x,y) in d1.items():
    print(x,'======',y)

print("=====nested dic=========")

family1={
    "child1":{
        "name":"Emily",
        "year":2004,
    },
    "child2":{
        "name":"John",
        "year":2014,
    },
    "child3":{
        "name":"Mark",
        "year":2008,
    },
}

child1={
        "name":"Emily",
        "year":2004,
    }

child2={
        "name":"John",
        "year":2014,
    }

child3={
        "name":"Mark",
        "year":2008,
    }

family2={
    "child1":child1,
    "child2":child2,
    "child3":child3,
}

print(family1["child3"])
print(family1["child3"]['name'])

print(family2["child3"]['name'])
