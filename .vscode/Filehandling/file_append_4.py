import os
di=os.getcwd()
print(di)
try:
    f_obj=open("F:\PythonDjango\.vscode\Filehandling\example.txt","a+")
    if f_obj.writable:
         f_obj.write("This is my first example ")
    if f_obj.readable:
        #print(f_obj.seek())
        print(f_obj.tell())             
        #given output 48,72.. it is the last character of the string "This is my first example" from the file
        #indicates the current idex of the string here above it is at the end
        f_obj.seek
        f_obj.seek(10)
        #is my first example
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