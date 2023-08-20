#create 2 dict and try t0 concatenate them
x=dict()
print(x)
l1=[(1,"one"),(2,"two"),("mahesh","hello")]
d1=dict(l1)
print(type(d1))
print(d1)
# d1.pop()            #error pop expected at least 1 argument, got 0
# print(d1)
# d1.pop('mahesh')
# print(d1)           #{1: 'one', 'mahesh': 'hello'}
# l2=[(1,"one","hi"),(2,"two"),("mahesh","hello")]    #       ^^^^^^^^
# ValueError: dictionary update sequence element #ValueError: dictionary update sequence element #0 has length 3; 2 is required
# d2=dict(l2)
# print(d2)
# d1.pop('mahesh')            #{1: 'one', 2: 'two'}
# print(d1)  

# d1.popitem()            #this will be fine will work like our previous pop LIFO
# print(d1)               #{1: 'one', 2: 'two'}

#for any dictionary to take out must give the key value corresponding
#no add but update is available
d1.update({5:"five",6:"six"})       #must supply the key and values when adding(updating)
print(d1)                           #{1: 'one', 2: 'two', 'mahesh': 'hello', 5: 'five', 6: 'six'}
#since no concatenation is possible but update can does the same operation
d2={'7':"seven",8:"eight"}      #another way of update with 2 dictionary   
d1.update(d2)       
print(d1)                       #{1: 'one', 2: 'two', 'mahesh': 'hello', 5: 'five', 6: 'six', '7': 'seven', 8: 'eight'}
#dictionary items, updated modified and deleted also
d3={1:'one',2:"Hi"} 
d1.update(d3)           
print(d1)
#output of above 31 to 33 line will be
#{1: 'one', 2: 'Hi', 'mahesh': 'hello', 5: 'five', 6: 'six', '7': 'seven', 8: 'eight'} 
for x in d1.keys():         # prints the keys of the dictionary
    print(x)
for y in d1.values():       #to print key values
    print(y)
for (x,y) in d1.items():    #prints both key and values of the dictionary   
    print(x,'---->',y)