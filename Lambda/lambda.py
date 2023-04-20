#They are anonymous functions 
#When they are used?
#*one-time use
#*I/O of other functions (they can be passed as input to higher order functions)
#*Reduce code size
#Syntax (lambda arguments:expression)
x=lambda a:a*a
print(x(3))
#Anonymous function with userdefined functions
def A(X):
    return(lambda y:X+y)
t=A(5)
print(t(5))
#Using lambda functions within filter(),map(),reduce()
#filter()
#used to filter the given iterables(lists,sets,etc) with the help of another function
#passed as an argument to test all the elements to be true of false
mylist=[1,2,3,4,5,6,7]
newlist=list(filter(lambda a:(a%3==0),mylist)) #Syntax: filllter(function ,iterables)
print(newlist)
#map
# Applies a given function to all the iterables and returns a new list
maplist=[1,2,3,4,5,6]
newmaplist=list(map(lambda a:(a/3!=2), maplist))
print(newmaplist)
#reduce
#Applies some other function to a list of elements that are passed as a parameter to it
#and finally returns a single value.
from functools import reduce 
print(reduce(lambda a,b:a+b,[23,56,43,98,1]))
#Lambda for Algebra
#Linear Equations
s=lambda a:a*a
print(s(4))
#3x+4y
d=lambda x,y:3*x+4*y
print(d(4,7))
#Quadratic equaion
q=lambda a,b:(a+b)**2
print(q(2,3))