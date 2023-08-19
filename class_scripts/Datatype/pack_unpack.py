# fruits=('grapes','banana','cherry')     #packed
# print(type(fruits))         #<class 'tuple'>
# (green,yellow,red)=fruits       #unpacked, muliple values to multiple values assigned
# print(green)                    #grapes
# print(yellow)                   #banana
# print(red)                      #cherry
''' since in above is kind of deep copy both fruits values and 
    greeen, yellow , red has shared the same memory location
    unpack and packing will hapen in line num 3
    now extended to list and dictionary this way
    3.5 is standard
    what version of python using
    in 3.7 and above pack and unpacking happens

'''
fruits=('grapes','banana','cherry','mango')
# (green,yellow,*red)=fruits
# print(green)        # grapes
# print(yellow)       # banana
# print(red)          # ['cherry', 'mango']
# (green,*yellow,red)=fruits
# print(green)            # grapes
# print(yellow)           #['banana', 'cherry']
# print(red)              #mango

(*green,yellow,red)=fruits
print(green)    #['grapes', 'banana']
print(yellow)   #cherry
print(red)      # ango


# (*green,*yellow,red)=fruits # this give error due to 2 stars can not be