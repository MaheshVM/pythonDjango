'''
is zip the values
'''
players=["sachin","richard","lara"]
sports=["cricket","chess","football"]

z=zip(players,sports)
print(z)            #<zip object at 0x00000299CA85E040>
print(list(z))      # [('sachin', 'cricket'), ('richard', 'chess'), ('lara', 'football')]

sports1=["cricket","chess","football","hocky"]
s=zip(players,sports)
print(list(s))              # [('sachin', 'cricket'), ('richard', 'chess'), ('lara', 'football')]
# obserece here in above since ther are 3 elements in players & 4 in sports it will ignore  the last one
#this makes as key

country=["india","pak","ban"]
m=zip(players,sports,country)
print(m)
#print(list(m))                  #[('sachin', 'cricket', 'india'), ('richard', 'chess', 'pak'), ('lara', 'football', 'ban')]
a,b,c=zip(*m)
print(a)
print(b)
print(c)