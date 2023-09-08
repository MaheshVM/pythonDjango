'''Files are used for storing the Data 
2 types of files based on data.
pdf,csv
video Files     - binary
text            - non binary
system generates huge log File
write a script to read file and particular data and analyse for the particular DeprecationWarning
    
Steps to handle the file are 
1. create connection to the File 
2.create a new file or read data from that File
3. close the file Connection

There are 14 modes of operation on file 
r  read a file , gives error if doesnt exist, 
w   will create for you, if not File 
a  append the file 
r+ read and write 
w+ write and read 
a+ append and read 
x  execution 

there are 7 other for binary also
rb
wb
ab 
rb+
wb+
ab+
xb+
Be a Part of Quora & stack oveflow must be member 
'''
#open('Filehandling/FirstFile.txt')      
#if not specified any mode default will be read mode.
f_obj=open('FirstFile.txt','w+')             # generaly over writes on every execution
#f_obj=open('FirstFile.txt','a')             # it will go on append at the end of every text
f_obj.write("My First file operation")      # thisline of code written in file FirstFile.txt
output=f_obj.read()
print(output)
# generaly curson at the end of the line text
f_obj.close()                               # must close the file on every operation

 
