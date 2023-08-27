listx=["A","B","C","D"]
y={} # empty dict
y=y.fromkeys(listx)
print(y) # {'A': None, 'B': None, 'C': None, 'D': None}

z={}

z=z.fromkeys(listx,45) 
print(z)