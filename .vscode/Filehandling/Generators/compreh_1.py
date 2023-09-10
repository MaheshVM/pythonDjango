'''
optimized way of writing for loop and while loop
can be easy to maintainenance & efficient

str1="mahesh"
out=[]
for letter in str1:
    out.append(letter)

print(out)
['m', 'a', 'h', 'e', 's', 'h']
this code we write efficiently in single line of code is nothing but comprehension
tuple to tuple
list to list
dictioanary to dictionary

Syntax:
list comprehension:
    [var <for loop>]
    [var for iterVar in iterable]
it is not necessary that var and iterVar must be same , var can be any expression
if only varibale name used must be same.
look at the below program. 
Note : left of for can be any expression as require
'''
str1="mahesh"
print([letter for letter in str1])
#['m', 'a', 'h', 'e', 's', 'h']     => look at this same as above in single line of code

str2="hello"
print([num+"hi" for num in str2])
#['hhi', 'ehi', 'lhi', 'lhi', 'ohi']        

num=[1,2,3,4,5,6]
sq=[n**2 for n in num]
print(sq)               
#[1, 4, 9, 16, 25, 36]

print(["Hello" for n in str1])
#['Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello']

x=.123
print([x for n in range(1,5)])
#[0.123, 0.123, 0.123, 0.123]

print([x**2 for x in range(11) if x%2==0])
#[0, 4, 16, 36, 64, 100]
