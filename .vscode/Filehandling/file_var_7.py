'''
writing the variable content to the file here
'''
cost=100
f_obj2=open("F:\PythonDjango\.vscode\Filehandling\sam2.txt","w+")
f_obj2.write(f"The head phone cost was {cost}")
f_obj2.seek(0)
out=f_obj2.read()
print(out)
f_obj2.close()      # mandatory to close the file after use