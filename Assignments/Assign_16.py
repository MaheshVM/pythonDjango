f1_text=open("F:\PythonDjango\.vscode/Filehandling\s1.txt","r")
f2_text=open("F:\PythonDjango\.vscode/Filehandling\s2.txt","r")
f1_text.seek(0)
f2_text.seek(0)
f1_out=f1_text.readlines()
f2_out=f2_text.readlines()
print(f1_out)
print(f2_out)
for line1 in f1_out:
    for line2 in f2_out:
        if line1==line2:
            print("same")
        else:
            print("not same")
            break

# ['My name is Mahesh,']
# ['My name is Mahesh']
# not same

# ['fadsfdsf dsfdsf afc ccxc']
# ['My name is Mahesh,']
# not same

# ['My name is Mahesh']
# ['My name is Mahesh']
# same
