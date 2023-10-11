'''
Better not to use print inside the constructor dunction
instance method:    means functions which are written inside the class are called instance method
instance variable : which can access using self in below explaination

inside the __init something which can not change will be stored and initilized here

'''
# class Car:
#     ''' constructor'''
#     def __init__(self,carb,model):
#         print(carb)
#         print(model)

#     def get_detail(self,variant,price,tag):
#         print(variant)
#         print(price)
#         print(tag)

# c1=Car("hyundai","i20")
# c1.get_detail("2022","10000","sports")


class Car:
    ''' constructor'''
    #variable here are called class variable
    def __init__(self,carb,model):
        self.carb=carb                    #object has initialized these are called "instance variable"
        self.model=model                   
    

    def get_detail(self,variant,price,tag):     # these are the local variables to this function
        # print(self.carb)                          # value taken from the constructor which has initialized instance variable
        # print(self.model)
        self.variant=variant
        self.price=price
        self.tag=tag
    def show(self):
        print(self.carb)
        print(self.model)
        print(self.variant)
        print(self.price)
        print(self.tag)
c1=Car("hyundai","i20",)
c1.get_detail('q5',5000,'v2')
c1.show()
print("==============variables outside the class========")
print(c1.carb)                                  #beauty of the python here outside the class also we can able to access here= hyundai
print(c1.price)                                 #same we can able to access it  =5000
print(c1.variant)                               #q5
c1.carb="maruti"
print(c1.carb)
