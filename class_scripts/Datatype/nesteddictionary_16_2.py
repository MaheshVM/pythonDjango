family1={
    'child1':{
            "name":"tanishka",
            "year":2011,
            "class": 6, 
    },
    "child2":{
            "name":"sreesh",
            "year":2020,
            "class":"lkg",
    },
    "child3":{
        "name":"raj",
        "year":2018,
        "class":2.
    },
}
child1={
            "name":"tanishka",
            "year":2011,
            "class": 6, 
}
child2={
            "name":"sreesh",
            "year":2020,
            "class":"lkg",
    }
child3={
        "name":"raj",
        "year":2018,
        "class":2.
    }

family2={
    "child1":child1,
    "child2":child2,
    "child3":child3
}

print(family1["child2"]["name"])        #if want any field must access with keys sreesh
print(family1["child1"]["year"])        #year of child1

print(child2["name"])                   #sreesh
print(child1["year"])                   #2011

print(family2["child2"]["name"])        #sreesh
print(family2["child1"]["year"])        #2011

print(family2["child1"])                #{'name': 'tanishka', 'year': 2011, 'class': 6}
print(family2["child2"])                #{'name': 'sreesh', 'year': 2020, 'class': 'lkg'}
print(family2["child3"])                #{'name': 'raj', 'year': 2018, 'class': 2.0}            