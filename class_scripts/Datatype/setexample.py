'''
set :
	it is a collection of heterogeneous data type which is unordered and changeable (mutable)
	
	set={}		//no empty set to be created	
	set()		// this way we can create using in built function
    they are unordered and no duplicates

'''
# setex={1,2,3,4}
# print(setex)        #{1, 2, 3, 4}

sety={1,2,3,4,"mahesh","vm",1,5,6,2}
print(sety)                         # {1, 2, 3, 4, 5, 6, 'vm', 'mahesh'}, on every execution position will change
# PS F:\PythonDjango> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.11.exe f:/PythonDjango/class_scripts/Datatype/setexample.py
# {1, 2, 3, 4, 5, 6, 'vm', 'mahesh'}
# PS F:\PythonDjango> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.11.exe f:/PythonDjango/class_scripts/Datatype/setexample.py
# {1, 2, 3, 4, 'mahesh', 5, 6, 'vm'}
# PS F:\PythonDjango> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.11.exe f:/PythonDjango/class_scripts/Datatype/setexample.py
# {1, 2, 3, 4, 5, 6, 'mahesh', 'vm'}
# PS F:\PythonDjango> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.11.exe f:/PythonDjango/class_scripts/Datatype/setexample.py
# {'vm', 1, 2, 3, 4, 5, 6, 'mahesh'}
# set will not follow indexing, as they save based on hash mechanism.
#they are non-subcriptable(indexing)
print(sety[4])                  # not allowed this indexing for set, if dont want to capture duplicate value we can use this setls