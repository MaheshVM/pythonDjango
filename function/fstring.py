cost=34.5
print("the cost of table is $",cost)

#the cost of table is $ 34.5
cost2=56.2
print("the cost of table is $",cost,"and it is on sale",cost2)

# Output:
# the cost of table is $ 34.5 and it is on sale 56.2
'''
some time insteadnot to break the flow we do use fstring with f
use variable with { } brackets
'''

# print("the cost of table is ${cost} and is available to sale at ${cost2}")      # $ is just a symbol

# output:
# the cost of table is ${cost} and is available to sale at ${cost2}

print(f"the cost of table is ${cost} and is available to sale at ${cost2}")

    # output:
    # the cost of table is $34.5 and is available to sale at $56.2

print(f"{4*5}")         #20