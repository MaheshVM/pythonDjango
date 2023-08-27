'''
if condition:
    block of code
elif condition:
    block of code
elif condition:
    block of code
else:
    block of code
'''

route = input("Enter the town you would like to go to: ")
if route == "Sarjapur":
    print("please take the Green line/Metro")
elif route == "Marathalli":
    print("please take the Orange line/Metro")
elif route == "HSR":
    print("please take the Yellow line/Metro")
elif route == "Kormangala":
    print("please take the Blue line/Metro")
else:
    print("Please input the correct route.")

if {1,2,3} == {1,3,2,1,2}:
    print("The lists match")
else:
    print("The lists do not match")

