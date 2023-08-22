#find the largest number in a given list
listx=[4,5,7,98,45,105]
lar=0
for l in listx:
    if l > lar:
        lar=l
print("largest: ",lar)

#output:
#105