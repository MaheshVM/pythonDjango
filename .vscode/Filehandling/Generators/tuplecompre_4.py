# tupel comprehension

str1="Mahesh"
val=(letter for letter in str1)
# val=[letter for letter in str1]     # did not worked out for list
#in tuple internally contains the yield so that will works out
print(val)      #<generator object <genexpr> at 0x0000016603960860>

s=next(val)
print(s)        #M
s=next(val)
print(s)        #a
s=next(val)
print(s)        #h
s=next(val)
print(s)        #e
# on request generating the loop, it will not iterate at once the for loop
