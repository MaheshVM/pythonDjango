#step value tells the direction of movement
listx=[1,2,3,4,5]
print(listx)
print(listx[2])
#print(listx[6])     # tells out of range
print(listx[2:4:1])  # [3, 4]

listy=[1,2,3,'mahesh',6,7,9.2]
print(listy)
print(listy[3][2:5])   #hes
print(listy[-4][-4:-1:1])  #hes

#list within list
person=['john',45,200.45,['french','english','spanish']]
print(person)                   #['john',45,200.45,['french','english','spanish']]
print(person[3])                 #   ['french', 'english', 'spanish']
print(person[3][0])              #   french
print(person[3][0][2:5:1])       #   enc
person1=['john',45,200.45,['french','english','spanish'],True]
print(person1[4])   
person3=['john',45,200.45,['french','english','spanish'],['python','C++','C'],True] 
print(person3[4])               #['python', 'C++', 'C']
print(person3[4][1])            #C++
print(person3[4][1][1:3])       #++
person4=['john',45,200.45,['french','english','spanish',['python','C++','C']],True]
print(person4[3][3])            #['python', 'C++', 'C']
print(person4[3][3][1][1:3])    #++
print(person4[3][-1][-2][-1:-3:-1])  #++

#naming convention example
list_of_even_nos=[2,4,6,8,10]
list_of_odd_nos=[1,3,5,7,9]
nos_upto_ten=list_of_even_nos+list_of_odd_nos
print(nos_upto_ten)     #[2, 4, 6, 8, 10, 1, 3, 5, 7, 9]




