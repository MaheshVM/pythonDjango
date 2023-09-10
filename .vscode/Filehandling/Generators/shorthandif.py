x=12
if x>10:print("It is greater than 10")  #this is short if
   # print("hello")                      # since this line wont works if given
   #else also wont works for the above

print("====================shor hand if============")
print("True") if x>10 else print("False")
#if condition of if is true then left side of expression executed other wise right side expression
#evaluated further can nest also
a=10
b=30
print("a is greater" if a>b else "b is greater")
#b is greater

p=60
q=100
r=30
print("p is greater" if p>q else "q is greater" if p>r else "r is greater" )
# #try look in left and right, if condition is true left is evaluated, in above p>q , condition fail
# goes to right side, there again full portion of else is right side again checks the condition
# p>r if true q is greater is evalued, other wise r is greater evalued
#dont put colon in short hand expression
#output:q is greater
