'''
seek()
tell()

'''
import os
di=os.getcwd()
print(di)
try:
    f_obj=open("F:\PythonDjango\.vscode\Filehandling\example.txt","w+")
    if f_obj.writable:
         f_obj.write("This is my first example")
    if f_obj.readable:
        #print(f_obj.seek())
        print(f_obj.tell())             
        #given output 24 it is the last character of the string "This is my first example" from the file
        #indicates the current idex of the string here above it is at the end
        #it tells the where is the file pointer now
        f_obj.seek(2)
        #out of the content "This is my first example"
        #is is my first example     will place the pointer at the 2 place there onward start reading
        #start from the position given and start reading the content
        output=f_obj.read()
        print(output)
    #f_obj=open("ex1.txt","w+")
    #try to copy the path from right click copy path
except Exception as e:
    print("The file does not exist",e)
finally:
    if f_obj.closed==False:
       # print("the file is still open")
        f_obj.close()                       # if not closed then you get the blank output
if f_obj.closed==False:
        print("opend the file outside")
        f_obj.close()