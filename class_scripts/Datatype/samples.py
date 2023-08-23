x=['c','v','c','f']
# count=0
# pos=0
# for n in x:
#     if n == 'c':
#         count+=1
#         print("position",pos)

# print(count)
# print(x.count('c'))

n=len(x)
print(n)
count=0
for i in range(n):
    if x[i] == 'c':
        count+=1
        print("position at c:",i)
print("total",count)

# position at c: 0
# position at c: 2
# total 2

