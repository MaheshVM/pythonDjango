# even=lambda a,b: a+10 if a > b else b+20
# x=even(6,3)
# print(x)

#output 16

# even=lambda a,b: a if a > b else b+20
# x=even(6,3)
# print(x)

#output 6


# even=lambda a,b: a if a > b else b+20
# x=even(6,30)
# print(x)

# output: 50

even=lambda a:a if(a%2==0) else a+30
x=even(7)
print(x)


#output: 37

even=lambda a:a if(a%2==0) else 20
x=even(7)
print(x)

#output: 20

lisx=[1,2,3,4]

def even_odd(n):
    if n % 2 == 0:
        return n+50
    else:
        return n+20
z=map(even_odd,lisx)
print(list(z))



