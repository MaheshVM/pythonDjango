'''
PEP : Python Enhance Propsal
requirement documents are maintained here, internal doc are maintained here
Genrator: Iterate on items , but iterate only ONCE.
only one time iterate, if multiple then again have to call
list,tuple are stored in heap(permananet) memory
generator stores in stack so it is faster, so better performance.
on equest generates data.
also called "LAZY Iterator"
lazy: because you request you get the data so it is called lazy
applicable to functions & class also
2 types of generators:
1. tuple cimprehension
2. function comprehension

for function generator: 
    any function giving keyword "yield"
    yeild hand in hand with 
'''
# print("------------Tuple comprehensive-------")
# str1="Mahesh"
# print((letter for letter in str1))

def myGen():
    yield
    # yield with expression
    for i in range(10):
        print(i)

next(myGen)      # this will requesting for data, for yield 
# for second data again have to call with next()