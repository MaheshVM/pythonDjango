'''
fix the file handling "error"
'''
try:
    f_obj=open("F:\PythonDjango\.vscode\Filehandling\example.txt","a+")
    if f_obj.writable:
         f_obj.write("This is my first example \n This my second example \n This is my Third error example")     #\n breaks the line in file
    if f_obj.readable:
        #print(f_obj.seek())
        print(f_obj.tell())             
        #given output 48,72.. it is the last character of the string "This is my first example" from the file
        #indicates the current idex of the string here above it is at the end
        # f_obj.seek
        f_obj.seek(0)
        #first example This is my first example
        output=f_obj.readlines()    #we get all content of the file 
        print(output)
        for word in output:
            if "error" in word:
                 print(word)
                 #print("Match found")
            # else:
            #      print("No error message in the file")
  
except Exception as e:
    print("The file does not exist",e)
finally:
    if f_obj.closed==False:
        print("the file is still open")
        f_obj.close()                       # if not closed then you get the blank output
if f_obj.closed==False:
        print("opend the file outside")
        f_obj.close()