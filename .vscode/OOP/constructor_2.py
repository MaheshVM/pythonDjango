# class Car:
#     def __init__(self, brand):    #local variable
#         print(brand)

# c=Car("hyundai")

# #hyundai

# class Car:
#     def __init__(self, brand,model):      #local variable
#         print(brand)
#         print(model)

# c=Car("hyundai","tb")

# hyundai
# tb

"""
multiple objects has separate memory location for each
instance method : function of the class is called instance method
"""
class Car:
    def __init__(self, brand,model):            #local variable
        print(brand)
        print(model)

c1=Car("hyundai","tb")
c2=Car("audi","cclass")

# output:
# hyundai
# tb
# audi
# cclass
