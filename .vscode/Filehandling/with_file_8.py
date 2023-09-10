'''
if used to open any file then python will automatically close the file
'''
with open("F:\PythonDjango\.vscode\Filehandling\withex.txt","w+") as with_obj:
    # as alias parameter give to the file with_obj ( it can be anything)
    try:
        if with_obj.writable:
            with_obj.write("this an example on with library")
        else:
            print("the file is not in write mode")
        if with_obj.seekable:
            with_obj.seek(0)
        else:
            print("the file is not in seekable mode")
        if with_obj.readable:
            content= with_obj.read()
            print(content)
        else:
            print("the file is not in readble mode")
        if with_obj.closed==False:
            print("still file is open")
    except Exception as msg:
        print("AN exception happens",msg)
    finally:
        if with_obj.closed == False:
            print("the file is till open")
        else:
            print("file is closed with finally block")

if with_obj.closed == False:
    print("the file is till open")
else:
    print("file is closed with finally block")