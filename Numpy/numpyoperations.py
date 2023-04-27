#Numpy Operations
#Find the dimension of the array
#Find the byte size of each element
#Find the data type of the elements
import numpy as np
a=np.array([(1,2,3),(2,3,5)])
print(a.ndim)#shows dimension
print(a.itemsize)#shows each element size
print(a.dtype)#shows each data type
print(a.size)#size of the array
print(a.shape)#Shows the shape of an array
#Reshaping
b=np.array([(1,2,3,4),(3,4,5,6),(7,8,9,10)])
c=np.array([(1,2,3,4),(3,4,5,6)])
print(b)
a=c.reshape(4,2)
print(a)
print(b[0:,3])#0 th row 3 index only
print(b[0:2,3])#0 th upto 2 row 3 element
a=np.linspace(1, 3,10)#ten values between 1 to 3
print(a)