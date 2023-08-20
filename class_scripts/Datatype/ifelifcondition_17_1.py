'''
if condition:
    block of code
elif condition:
    block of code
elif condirion:
    block of code
else:
    block of code

syntax of
'''
# route=input("Enter the town name like to travel: ")
# route=route.lower()
# if route == "sarjapur":
#     print("please take the green metro")
# elif route == "marathahalli":
#     print("take oranage metro")
# elif route == "Koramangala":
#     print("take the yello metro")
# elif route == "HSR":
#     print("take the blue metro")
# else:
#     print("please enter the correct roue")

# if [1,2,3] == [1,3,2]:
#     print("the list match")
# else:
#     print("the list do not match")

# if {1,2,3}=={1,3,2}:        # because set do not follow ordering so matches
#     print("matches")
# else:
#     print("do not match")

#for loop
#any thing inside the for loop is temporary memory locations, is called stack memory location
# refer the book diagram for reference to understand 
# listx=[1,2,3,4]
# for x in listx:
#     print(x)

# print(x)            #it is stored with value 4 last value

# listy=(1,2,3,4)
# for y in listx:
#     print(y)
# print("----------------------------")
# listz={1,2,3,4,5,5,6,6,1,1}             
# for z in listz:
#     print(z)                # 1,2,3,4,5,6

# listd={
#         "one":1,
#         "two":2,
#         "three":3,
# }
# for d in listd:
#     print(d)        # one, two, three all keys will be taken here

# name="Mahesh"
# for n in name:
#     print("hi"+n)       # n will take M, a, h, e,s, h


# cars=["audi","maruti","tata","hyundai"]
# for c in cars:
#     print(c)            #audi, maruti, tatat
#     if c == "tata":     
# #         break
# cars=["audi","maruti","tata","hyundai"]
# for c in cars:
#     if c == "tata":     
#         break
#     print(c)            #audi, maruti

# fruits=("orange","grapes",'mango',"cherry")
# for fruit in fruits:
#     print(fruit)                    # orange
#     if fruit !="grapes":        
#         break


fruits=("orange","grapes",'mango',"cherry")
for fruit in fruits:
    print(fruit)                    # orange, grapes,mango, cherry
    if fruit !="grapes":        
        continue