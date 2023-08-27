# iterate over a sequence and do selective stuff based on the condition
# for iterationVariable in Sequence/Map:
#   lines of code for for loop

listx=[1,2,3,4,4,3,4,3]
for x in listx:
    print(x)

print("outside the for loop")
print(x)

for letter in "Ankit":
    print( "hi" + letter)

print("======conditions======")
cars=["Audi","RR",'MERC','BMW','Hyundai']
for car in cars:
    
    if car == "BMW":
        break # breaks the current iteration and exits outside of the for loop righ then and there.
    print(car)
print("outside the for loop")

fruits=("orange","banana","grapes","cherries")
for fruit in fruits:
    print(fruit) #orange....
    if fruit=="grapes":
        break

print("========continue=========")
for fruit in fruits:
    
    if fruit=="grapes":
        continue # breaks the current iteration and skips or continue to the next iteration.
    print(fruit)

