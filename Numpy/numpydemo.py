#Numpy
#Numpy is the core library for scientific computing in python
#It provides a high performance multidimensional array object and tools for working with these arrays.
import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a)
#Advantages of numpy over List
#Less Memory,fast,convinent
#Memory Demo
import sys
import time
s=range(1000)
print(sys.getsizeof(5)*len(s))
D=np.array(1000)
print(D.size*D.itemsize)
print("-----------")
#fast demo
size=10000000
l1=range(size)
l2=range(size)
a1=np.arange(size)
a2=np.arange(size)
start=time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)
start=time.time()
result=a1+a2
print((time.time()-start)*1000)