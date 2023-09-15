x=10

def f():
    global x
    x=x+20
    print(x)                    #30          

print("before call",x)          #10
f()
x=x+50              
print("outside the main",x)     #80