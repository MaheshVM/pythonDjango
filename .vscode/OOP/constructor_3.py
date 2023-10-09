class Car:
    ''' constructor'''
    def __init__(self,carb,model):
        print(carb)
        print(model)

    def get_detail(self,variant,price,tag):
        print(variant)
        print(price)
        print(tag)

c1=Car("hyundai","i20")
c1.get_detail("2022","10000","sports")