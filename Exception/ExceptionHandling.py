#Exception 
#An Exception is an event,which occurs during the exceution of a program, that disrupts the normal flow of the program's instruction.
#Exception Handling
#Process of responding to the occurance, during computation, of exceptional conditions requried special processing - often changing the normal flow of program execution
#Process of exception handling
#try    - keyword used to keep the code segment under check
#except - segment to handle the exception after catching it
#else   - Run this when no exception exist
#finally- No matter what run this code
#Raising an exception
# we can use raise to raise an exception
#Order try->execpt->else->finally
x=5
if(x>5):
    raise Exception("X should not exeed 5 , {}".format(x))
#AssertionError Exception
#Tests if the condition is true
import sys
assert('Linux' in sys.platform),"This runs only on Linux"