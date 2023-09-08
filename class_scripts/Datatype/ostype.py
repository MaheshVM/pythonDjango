import os
print(os.name)      # name of the os nt
print(os.getcwd())    # current working diectory  F:\PythonDjango
#os.mkdir('test')       # creates a directory in current working directory
#directory creates and deletes
try:
    os.mkdir('ex')
   # os.rmdir('ex')
except FileExistsError:
    print("directory not delete")
#os.rmdir('test')
finally:
    os.rmdir('ex')