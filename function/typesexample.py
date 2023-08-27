'''
in input have to give type what it is returning
'''
# age=int(input("enter age of person :"))
# print(age)
# print(type(age))            # this will take in to integer here

# lets say some one wnated to enter as age 18.5
'''then will give Error
enter age of person :45.5
Traceback (most recent call last):
  File "f:\PythonDjango\function\typesexample.py", line 4, in <module>
    age=int(input("enter age of person :"))
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '45.5' 
then how we can handle it using "eval"
'''
# x=3
# print(eval(x))          #error here TypeError: eval() arg 1 must be a string, bytes or code object

# x='3.5'
# print(eval(x))          # this will give 3.5


age=eval(input("enter age of person :"))    # this eval will evaluate based on the input what you give integer value int, float value float type
print(age)                                  # eval will does automatically all the conversion
print(type(age)) 

# output of line 25 -27
# enter age of person :56.4
# 56.4
# <class 'float'>

# enter age of person :56
# 56
# <class 'int'>    
# 
# enter age of person :"mahesh"
# mahesh
# <class 'str'> 