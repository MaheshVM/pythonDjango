sport='basketball is a sport'
print(sport[14])

name='Naveen' # vee.
print(name[2])


print("========slicing======")
#[start index:stop index(-1):step value(default =+1)] 
# step value tells you the direction of movement - rememeber the +ve axis and -ve axis eg
print(name[2:6])

# l is a s
print(sport[4:20:3]) # ---> sport[10:19:1]

print("=======negative indexing========")

string1='Rajneesh'
print(string1[3])
print(string1[-5])
print(string1[6])
print(string1[-2])
print(string1[-7])

print(string1[-3:-8:-2])

name="MoM"
name1="MalyalaM"

print(string1[::1])
print(string1[::-1])
#print(name[::])

str1='MoM'


if str1[::] == str1[::-1]:
    print("String is a pallindrome")
else:
    print("String is not a pallindrome")



