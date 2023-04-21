#MAP
# It applies a given function to all the iterables and returns a new list.
#map(func,iterables)
def new(a):
    return a*a
x=map(new, [1,2,3,4])
print(list(x))
#map function can take more than one parameter
def newL(a,b):
    return a*b
x=map(newL, [1,2,3,4],[2,3,4,5])
print(list(x))
#lambda functions with other functions
lst=[1,2,3,4,5]
y=list(map(lambda x:x+3,lst))
print(y)
#Filter
#used to filter the given iterables lists,sets,etc. with the help of another function passed as an argument
#to test all the elements to be true or false
def new1(i):
    if i>=3:
        return i
j=filter(new1, [1,2,3,4,5,6,7,8,9])
print(list(j))
#filter with lambda
k=filter(lambda a:(a>=3), [1,2,3,4,5,6,7,8,9])
print(list(k))
#reduce()
#Applies some other function to a list of elements that are passed as a parameter
#to it and finally returns a single value.
from functools import reduce
l=reduce(lambda x,y:x+y, [1,3,4,5,6,7,7,8,8])
print(l)
#filter() within map()
c=map(lambda x:x+x, filter(lambda x:(x>=4), [2,3,4,5]))
print(list(c))
#map() with filter()
d=filter(lambda x:(x>=4), map(lambda x:x+x, [2,3,4,5,6]))
print(list(d))
#map() and filter() within reduce()
r=reduce(lambda x,y:x+y, map(lambda x:x+x, filter(lambda x: (x<=4), [1,2,3,4,5,6,7])))
print(r)