# perform n+f(n-1)

def recursive_function(n):
    if (n>0):
        result=n+recursive_function(n-1)
        #print(result)
    else:
        result=0
    return result

print("Recursive example")
print(recursive_function(4))
         