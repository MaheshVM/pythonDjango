'''
program creates a directory in specific directory in specific difrectory as you 
want here created mahesh folder in c:/ path
'''
import os
#os.mkdir("sampl")
workd=os.getcwd()
# os.chdir("../sampl")
parent='C:/'
directory="mahesh"
path=os.path.join(parent,directory)
os.mkdir(path)
dir_list=os.listdir(workd)
print(dir_list)
#['.git', '.vscode', 'Assignments', 'class_scripts', 'function', 'indexing.py', 'intro.py', 'listoperation.py', 'mahesh', 'sampl', 'secondclass.py']