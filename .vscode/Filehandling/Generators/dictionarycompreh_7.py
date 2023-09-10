#set comprehension
s={d for d in range(10)}
print(s)                #  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# dictinary comprehension
# one of the method
k={(n,) for n in range(5)}
print(type(k))
print(k)            #{(2,), (4,), (1,), (0,), (3,)}

# second method
k2={num:num*5 for num in range(5)}
print(k2)                           #{0: 0, 1: 5, 2: 10, 3: 15, 4: 20}
#why tuple comprehension will create not set or dictionary

person={
    'name':'mahesh',
    'place':'pune',
    'country':'India',

}

d2={p for p in person.keys()}
print(d2)                       #{'place', 'name', 'country'}   it becomes again set

d2={p for p in person.items()}  #this makes unordered dictioanary
print(d2)                       #{('place', 'pune'), ('name', 'mahesh'), ('country', 'India')}

d3={p:v for p,v in person.items()}
print(d3)                       #{'name': 'mahesh', 'place': 'pune', 'country': 'India'}

d3={p:v for p in person.keys() for v in person.values()}
print(d3)                       #{'name': 'India', 'place': 'India', 'country': 'India'}
#since values of the key are mutable changes with overriding previous value so we get the India all the time here