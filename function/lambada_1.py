# x=lambda a,b:(a+b,a-b,a*b)
# print(x(2,4))

# output:
# (6, -2, 8)

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(11))
