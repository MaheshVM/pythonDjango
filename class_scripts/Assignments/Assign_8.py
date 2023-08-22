# adding 50 to even list and 25 to odd list
even_num=[]
odd_num=[]
for n in range(1,100):
    if n % 2 == 0:
        even_num.append(n+50)
    else:
        odd_num.append(n+25)
print(even_num)
print(odd_num)