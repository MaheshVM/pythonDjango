person= {
    'name':"Mark",
    'age':55,
    "city":"Boston",
}

for dictVarKey,dictVarValue in person.items():
    print(dictVarKey,"=====",dictVarValue)



for char in "Python":
    
    if char !='o':
        print(char)
        #continue - this is redundant peice of code hence more optimized without it.
    else:
        break
