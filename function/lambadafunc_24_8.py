# def lamb_fun(n):
#     return lambda a:a**2

# x=lamb_fun(4)  #here 4 is substitured in n=4
# print(x(3))         #9    , after calling lambda function 3 willbe assigned to a=3, so 3*3=9

def lamb_fun(n):
    return lambda a:a**n

x=lamb_fun(4)               # this will be substituted in n=4
print(x)                    #<function lamb_fun.<locals>.<lambda> at 0x00000265350553A0>
print(x(3))         #81, now here a=3, n=4  so 3**4=81   

# def lamb_fun(n):
#      lambda a:a**n


#  z=lamb_fun(2)            # this will be substituted in n=4
#  print(z)
# print(z(3))         #81, now here a=3, n=4  so 3**4=81  

# Output:
# error