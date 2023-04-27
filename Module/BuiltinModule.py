#Build in modules are written in c and interpreted using python interpreter.
#__builtin__
# print(help('modules'))
import Module
print(dir(Module))
#python module search path
#When we import a module, Python searches for the module at certain places.
#If it cannot find the module in the builtin modules, it searches through the list in the sys.path
#Search moudule order
#Current Directory -> PYTHONPATH -> Default - Directory
import sys
print(sys.path)
import datetime
print(datetime.date.today())