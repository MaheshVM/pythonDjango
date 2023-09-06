# x=lambda a,b:(a+b,a-b,a*b)
# print(x(2,4))

# output:
# (6, -2, 8)
'''
Recursive function
function will call by itself
based on condition must be terminated

lambada mean anonymous
it is a non named function, but mentioned with keyword "lambada"
lambada can take any number of arguments. but must have only one expresssion
syntax:
  lambada parameter_list: expression
'''
adding_two_nos=lambda a,b:a+b

print(adding_two_nos)   #<function <lambda> at 0x000002069C8E6160>
print(adding_two_nos(4,5))    #9
# in above it shows that variable adding_two_nos points to the lambda function address #<function <lambda> at 0x000002069C8E6160>

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(11))    #44
