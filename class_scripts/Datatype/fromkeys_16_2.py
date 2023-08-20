'''
when using in built function use emty dictionary
below program creates dictionary from the list
'''
listx=['one','two','three']
y={}        # create empty dictionary
y=y.fromkeys(listx)
print(y)                # 'one': None, 'two': None, 'three': None}

# can be the keys values will be same
z={}
z=z.fromkeys(listx,"hi")
print(z)                    # {'one': 'hi', 'two': 'hi', 'three': 'hi'}

listy=(1,2,3)               #creating dictionary from tuple
p={}
p=p.fromkeys(listy,"we")        #{1: 'we', 2: 'we', 3: 'we'}
print(p)

for (m,n) in p.items():
    print(m,n)