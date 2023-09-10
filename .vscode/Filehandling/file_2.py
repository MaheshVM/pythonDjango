import os
di=os.getcwd()
print(di)
try:
    f_obj=open("F:\PythonDjango\.vscode\Filehandling\example.txt","w+")
    if f_obj.writable:
         f_obj.write("This is my first example")
    if f_obj.readable:
        output=f_obj.read()
        print(output)
    #f_obj=open("ex1.txt","w+")
    #try to copy the path from right click copy path
except Exception as e:
    print("The file does not exist",e)
finally:
    if f_obj.closed==False:
        print("the file is still open")
        f_obj.close()                       # if not closed then you get the blank output
if f_obj.closed==False:
        print("opend the file outside")
        f_obj.close()