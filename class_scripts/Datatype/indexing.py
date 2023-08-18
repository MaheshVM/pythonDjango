sport="basketball"
msg="welcome to the python program"
print(sport[5])
name='Mahesh'
print(name)
print(name[3])
print("---------------------slicing--------------")
#formula on indexing [start index:stop index(-1):step value]
#-1 here means have to go 1 value before 
print(name[2:5:1])
print(msg[15:21:1])
print(name[2:7:1])
print(name[2:20:1])
#anything after last char will be considered as space, python will be smart enough to understand last character
print(msg[15:26:2]) #has 2 step value
print(msg[10:26:3])

print("-----------------negative indexing----------------")
string1="Raghavendra"
print(string1[3])       # same value h
print(string1[-8])      #same value h
print(string1[6])
print(string1[-5])
print(string1[-11:-8])      #prints Rag
print(string1[-11:-8:1])     #Rag
#-ve step goes in left side 
#step value tells the direction of movement in negative also must be +1, +2 like this
print(string1[-9:-12:-1])       #print gaR
#step value tells the direction of moeement
print(string1[-9:-11:-2])

h
h
e
e
Rag
Rag
gaR
g