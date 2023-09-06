'''
must identify the best possible error may occur
'''
try:
    listx=[1,2,3,4]
    print(listx[90])
except Exception as e_msg:
    print("May be out",e_msg)

# #output
# May be out list index out of range