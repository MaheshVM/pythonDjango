# for num in 55:
#     print(num)          #error

# for x in (55):
#     print(x)        #TypeError: 'int' object is not iterable

# for x in (55,):     # tuple with single element
#     print(x)        # 55

person={
    'name':"Mahesh",
     'age': 45,
    "city":"pune",
}

for dic in person:
    print(dic)          # prints the keys of the dictionary

for dic in person.keys():
    print(dic)          #prints the keys of the dictionary

for dic in person.values():     # this will still takes as list 
    print(dic)              # prints all values of the key

for x in person.keys():
    print(person[x])            # it will print all the values of the keys

for y in person:
    print(person[y])            # prints all the values of the keys

for z in person.items():    
    print(z)
# ('name', 'Mahesh')  output of line 31 to 32 
# ('age', 45)
# ('city', 'pune')

for (x,y) in person.items():
    print(x,"------",y)

for char in "Python":
    if char != 'o':
        print(char)             #p
        break

for char in "Python":
    if char != 'o':
        print(char)             #p
    break

for char in "Python":
    if char != 'o':
        print(char)             #p, y ,t,h
        continue
    else:
        break               

for char in "Python":
    if char != 'o':
        print(char)             #p, y ,t,h, it is more redundant code and optimized 
    else:
        break  

