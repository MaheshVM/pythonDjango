# list -> combination of other data types under one. or combination of heterogenous datatype.
# create a list: a. listVar=[multiple elements seperated by a comma] eg listx=[1,2,3,4,5] 
# b. list() - inbuilt function()
# empty list -> listx=[]
listx=[1,2,3,4,5]
print(listx[2:4:1]) # 3,4,5  .....[3,4]
print(listx[-1])

listy=[1,2,'ankit','Naveen',6,7,9.90] # vee
print(listy[3][2:5:1]) # listy[3] -->"Naveen"[2:5:1] --> vee

person=['John',45,200.45,['French','Spanish','English'],True] # ani from spanish
print(person[3][1][2:5]) # person[3] -->['French','Spanish','English'][1] --> "Spanish"[2:5]  

person1=['John',45,200.45,['French','Spanish','English'],['Python','C',"C++",'Java'],True] # ++
print(person1[4][2]) # person[3] -->['French','Spanish','English'][1] --> "Spanish"[2:5]  

person2=['John',45,200.45,['French','Spanish','English',['Python','C',"C++",'Java']],True] # ++
print(person2[3][-1][-2][-1:-3:-1]) 
print(person2[3][3][2][1:3])
print(person2[-2][-1][-2][-1:-3:-1]) 

# naming convention - best coding practices
'''
a. var name, function names, class names, etc  should be be relevant and meaningfull
b. two styles - just choose one and follow the same everywhere
    1. listOfNumbers = [1,2,3,4,5]
    2. list_of_numbers=[1,2,3,4,5]
    eg list_of_even_nos=[2,4,6,8,10]  and NOT x=[2,4,6,8]

'''

list_of_even_nos=[2,4,6,8,10]
list_of_odd_nos=[1,3,5,7,9]

nos_upto_ten=list_of_odd_nos + list_of_even_nos # [1,2,3,4,5,6,7,8,9,10].......[3,7,11,...]....error....[1, 3, 5, 7, 9, 2, 4, 6, 8, 10] (concatenation).....
print(nos_upto_ten)

