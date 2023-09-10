# random person generator 
import random, time
regions=['asia','usa','europe']
country=['india','ny','london']


def people(num):
    result=[]
    for i in range(num):
        person={
            'id':i,
            'region':random.choice(regions),
            'country':random.choice(country),
        }
        result.append(person)
    return result

result=people(2)
print(result)
# [{'id': 0, 'region': 'europe', 'country': 'london'}, {'id': 1, 'region': 'europe', 'country': 'london'}]


def people_gen(num):
    for i in range(num):
        person={
            'id':random.randint(1,num),
            'region':random.choice(regions),
            'country':random.choice(country),
        }
        yield person

# n=10
# for i in range(n):
#     print(next(people_gen(n)))  

#time performance measurement

print("by regualr finction time aken")
t1=time.perf_counter()
result=people(10)
#print(result)
t2=time.perf_counter()

print("using generator time taken")
t3=time.perf_counter()
n=10
for i in range(n):
    print(next(people_gen(n)))  
t4=time.perf_counter()

print("time taken by regular function:",t2-t1)

print("time taken by generator:", t4-t3)

    
