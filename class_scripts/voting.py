#age=16 # assignment as = assignment operator
# == - comparison operator, compare left and right values and return True or False
# >=, <=, !=
age=int(input("Enter the age of the person: "))
# age="18" # input() always stores the value as a string.
#age=int(age)


if age>=18: # "18">=18
    print("you are eligible to vote")
    print("this is the second line if the cond is true")
else:
    print("you are not eligible to vote")
    print("this is the second line if the cond is false")
    
print("Outside of the if-else")