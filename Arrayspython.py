#Array is basicall a data structure which can hold more than one value at a time.
#it is a collection of ordered series of elements of the same type.
#List vs Array
#Arrays can store only one single data type where as list can store multiple data types of data.
#The kind of operations on both are different 
#Arrays in python can be created after importing the array module
#import array or import array as a from array import*
import array as ar
#module name array or ar and then the data type
a=ar.array('i',[1,2,3,4,5,6,7])
print(a)
#from array import * 
from array import *
b=array('i',[2,3,4,5])
print(b)
print(b[2])
print(b[-1])
#Basic Array Operations
print(len(b))
#Adding elements to an array
#append() add single element at the end of the array
#extend()add more than one element to the end of the array
#Insert() add elements at the specific position
from array import *
c=array('i',[1,2,3,4,5,6])
print(c)
c.append(9)
print(c)
c.extend([7,8,9,10])
print(c)
c.insert(1,11)
print(c)
#Removing elements in an array
#pop() Used when we want to remove an element and return it
#remove() is used to remove an element with a specific value without returning it
print(c.pop())
c.remove(11)
print(c)
#Array Concardination
#Array Concardination can be done using + symbol
import array as arr
a=arr.array('d',[1.1,2.2,3.3,4.4,5.5])
b=arr.array('d',[6.1,7.2,8.3,9.4,10.5])
c=arr.array('d')
c=a+b
print("Array c is ",c)
#Slicing an Array
#An Array can be sliced using the : symbol. This returns a range of elements that we have specified by the 
#index numbers
import array as arr
a=arr.array('d',[1.1,2.2,3.3,4.4])
print(a[0:3])