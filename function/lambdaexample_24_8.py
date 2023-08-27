# area_of_cube=lambda l,b,h:l*b*h

# print(area_of_cube(4,5,6))

# area_of_cube=lambda l,b,*h:l*b*h

# print(area_of_cube(1,2,3))      # evaluation will lambd(1,2,(3))=>1*2*(3,)=> 2*(3,)=>(3,3)    tupel value added with same value
# #number=1,                       # as interpreter treat as the tuple of 1 element.(1,)
# print(area_of_cube(3,3,3))      #(3, 3, 3, 3, 3, 3, 3, 3, 3)

    #output:
    #(3, 3)

    #lambda within the function

    def lamb_fun(n):
        return lambda a:a**2

    print(lamb_fun(4))

    # output will be 
    #<function lamb_fun.<locals>.<lambda> at 0x000002C5D7A55300>

    def lamb_fun(n):
        return lambda a:a**2

    x=lamb_fun(4)
    print(x)
    print(x(3))

# Out put:
# <function lamb_fun.<locals>.<lambda> at 0x0000010856B554E0>
# <function lamb_fun.<locals>.<lambda> at 0x00000108567D6160>
# 9


