'''
1
22
333
4444
----
'''
for i in range(1,5):
    #print(i)            #automatcally puts new line
    for j in range(i):
        print(i,end='')  # replaces the \n of print with that character
    print()             # simply a \n or enter