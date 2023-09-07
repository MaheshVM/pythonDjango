import sys
import math

print(sys.version)

# 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)]
#print(sys.modules)

#print(sys.argv)                 #'f:/PythonDjango/class_scripts/modules/sysmodule.py'] since it give the path of the module
# if giving arguments through command line argument
print(sys.path)
#
#sys.exit()                  #makes hard exit for the system
# some time any dead lock there can use to exit.
# after exit no statements are executed
#sys.exit(0)     # indiacates gracefull shutdown, anything other than 0 will be forcible shutdown
#os._exit()      # killing the kernelprocess, whole kernel will get killed

print(sys.api_version)      #1013
print(sys.maxsize)          #9223372036854775807

# maxsize 
print(math.pow(2,63)-1)     #9.223372036854776e+18

