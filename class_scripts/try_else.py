# if exception thrown and dont want to execute another code , then else block
#f exception thrown no else block
#finally will be the default that will get executed

# try:
#     a=2
#     b=4
#     print(a/b)
# except Exception as msg:
#     print("Exception raised ",msg)
# else:
#     print("Else code block")

# 0.5
# Else code block

# try:
#     a=2
#     b=0
#     print(a/b)
# except Exception as msg:
#     print("Exception raised ",msg)
# else:
#     print("Else code block")

# #Exception raised  division by zero

try:
    a=2
    b=0
    print(a/b)
except Exception as msg:
    print("Exception raised ",msg)
else:
    print("Else code block")
finally:
    print("always printed final")

# 0.6666666666666666
# Else code block
# always printed final

# Exception raised  division by zero
# always printed final
# see in above finally will be always executed 

# finally will exceuted exception occurs or not