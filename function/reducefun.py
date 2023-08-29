'''
reduce:
it is not part of the python in built, we need to import

'''
from functools import reduce        # file reduce imported from functools
listx=[1,2,3,4,5,6]
#print(sum(listx))

# result=reduce(lambda x,y:x+y,listx)     # reduce gives 1 value integer or float
# print(result)

# since reduce can be used for mean.mode,median and average functional operations.
# it gives one value. if mean then formula will be in place of x+y above
import statistics
mean_m=lambda x:statistics.mean(listx)

p=mean_m(listx)
print(p)

# #output
# 3.5

mode_m=

              