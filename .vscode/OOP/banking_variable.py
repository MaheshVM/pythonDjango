'''
instance variable: used with an instance a variable that is defined inside a method and constructor. variable defined inside the methods 
                    is called instance variable
static variable: is a class variable, outside of instance method and constructor. is nothing but variables defined inside the class
                are called static variable
local variable: variables defined inside the method are called local
global variable: scope of the variable is globally, and defined in same py. it is outside the class variable

variable if not changes must be defined inside the constructor, for example name, emp code etc..
'''

# class Customer():
#     ''' bankong operation performed here'''
#     def __init__(self,name,accno):
#         loans=4         #local variabe to the constructor
#         self.name=name      #instance variable
#         self.accno=accno    
#     def display(self):
#         loans=2
#         print("customer name",self.name)
#         print("customer account",self.accno)
#         print("Total loans of customer",loans)


# c1=Customer("mahesh",1234)
# c1.display()



# class Customer():
#     ''' bankong operation performed here'''
#     bank_name="DB"
#     def __init__(self,name,accno):
#         loans=4         #local variabe to the constructor
#         self.name=name      #instance variable
#         self.accno=accno    
#     def display(self):
#         loans=2
#         print("customer name",self.name)
#         print("customer account",self.accno)
#         print("Total loans of customer",loans)
#         print("class variable outside the class",self.customer_loan)    # here it give error becuase look at the calling after 
#                                                                         # variable is initialized or declared


# c1=Customer("mahesh",1234)
# print("bank name",c1.bank_name)
# #c1.display()
# c2=Customer("vijay",3456)
# print("Vijays bank name",c2.bank_name)
# c2.display()
# c1.customer_loan=1000                   #it become instance variable
# print("my class variable",c1.customer_loan)
# c1.display()

#this above is error, in calling the variable and function lines

class Customer():
    ''' bankong operation performed here'''
    bank_name="DB"
    def __init__(self,name,accno):              #instance method
        loans=4         #local variabe to the constructor
        self.name=name      #instance variable
        self.accno=accno    
        Customer.bankcity="India"           # this becomes the class variable applicable to all
    def display(self):                      #class method it is not instance method
        loans=2
        print("customer name",self.name)
        print("customer account",self.accno)
        print("Total loans of customer",loans)
        print("class variable outside the class",self.customer_loan)    # here it give error becuase look at the calling after 
                                                                        # variable is initialized or declared
        print("variable declared outside the class",self.abc)           #now this variable declared outside the class still we can able to accees it
    
    @classmethod                #decorator, this modfies to all the objects created
    def bankdetail(dls):
        dls.bankfounder="pqrst"
        print("Bank founded by",dls.bankfounder,"Bank name",dls.bank_name)
    
    #static method/utolity method
    @staticmethod
    def totalcustomer(x):
        print("total number of customer",x)

c1=Customer("mahesh",1234)              #at this moment customer_loan variable is not initialized at this point
print("bank name",c1.bank_name)
c1.customer_loan=10000                      # variable can be declared outside and used inside the class also
#c1.display()
Customer.account_type="saving"          # this is the way declared 
print(Customer.account_type)
c2=Customer("vijay",456)
print("class c2 customer accont",c2.account_type)   #class c2 customer accont saving
#print("i am in class2",c2.customer_loan)            #  since this variable initialized only within class c1 not in c2
Customer.abc="hello"
print("inside the class1",c1.abc)           #now if referenced with class name we can initialized to the abc variable can be 
print("inside the class2",c2.abc)           # accces in both the objects

# inside the class1 hello
# inside the class2 hello
c1.display()
print(c1.bankcity)              #India
print(c2.bankcity)              #India
Customer.bankdetail()           #Bank founded by pqrst Bank name DB, define class method
c2.bankdetail()                 #Bank founded by pqrst Bank name DB
c1.bankdetail()                # Bank founded by pqrst Bank name DB  
Customer.totalcustomer(10)        #total number of customer 10  



# bank name DB
# saving
# class c2 customer accont saving
# inside the class1 hello
# inside the class2 hello
# customer name mahesh
# customer account 1234
# Total loans of customer 2
# class variable outside the class 10000
# variable declared outside the class hello
# India
# India