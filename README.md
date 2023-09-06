# pythonDjango

Exception : used to handle errors

parent of exception is : BaseException
mother of exception		: Exception

Exception is child Baseexception then tree goes down

file operations:
1. open a DB/file connection
2. add/modify/delete data 
3. update the DB and save it
4. close the connection file	(it is very much mandatory)
else will be in dangling pointer.

os._exit(1)		dont use this it will kill the python process
good practice to use try except block in side the program code.

Modules:

def: 
modules
packages
libraries
frameworks

module: any py file will be called as module
sys,time.os - modules
import -->used to call in built files

Package:
is a group of module under one. It is very important that must have an empty __init.py__ file(must be empty)
then it becomes as package.
we get alll the packages
ex: multiple py files under one folder
we can share to anybody if there is __init__.py

library:
is a group of packages under one.
ex: numpy,pandas, scipy  all are contains the packages and internally modules.

keeping the modules is accessibility
frameworks:
