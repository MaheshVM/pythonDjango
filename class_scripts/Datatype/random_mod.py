'''
if generate random data use random module
ex: password of ATM
'''
import random
# #randint required 2 values, range between 2 numbers
# print(random.randint(1,10))     # generates any random between 1 to 10
# print(random.random())          #generates float random number
# listx=[1,2,3,4]
# print(random.choice(listx))     # picks up any random from the listx

# setex={1,2,3,4,5,1,1,2,3,6} 
# print(random.choice(setex))     #choice wont work on set

# tuplex=(1,2,3,4,5,1,2,)
# print(random.choice(tuplex))        # get the any random value from tuple defined

'''
Descriptive and inferential Stats
Inferential sample
Descriptive complete data
statastical means complete data

population data - complete data
commualtive-probability of coming any number high because priority is given high
'''
# listx=[1,2,3,4,5]
# print(random.choices(listx,weights=[1,10,2,1,1],k=5))
# # here in above for the each element of listx given the weights , higher the value more the chances, k=5 number of elements
# # [3, 4, 3, 2, 2]
# # [5, 4, 2, 2, 3]
# # [5, 2, 2, 2, 3]
# #for any number higher weigt given more occurences as seen above, it may change as per requirement
# print(random.choices(listx,weights=[1,10,2,1,1],k=20))
#[2, 2, 5, 4, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2]   
#observed that for k only t was working took m,n did  not worked 

listy=[1,10,20,30,40]
random.shuffle(listy)        # works on mutable sequence
print(listy)

# listz=(1,30,50,55,60,70)    # 
# random.shuffle(listz)       #TypeError: 'tuple' object does not support item assignment, this wont work because it 
# print(listz)                # tuple is immutable so
# set does not works with shuffle
