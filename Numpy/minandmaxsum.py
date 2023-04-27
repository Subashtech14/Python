import numpy as np
a=np.array([1,2,3])
print(a.max())
print(a.min())
print(a.sum())
#Sum of axsis
a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])
print(a.sum(axis=1))
print(np.sqrt(a))
print(np.std(a))#standard  deviation
print(a+b) #sum of two array
print(a*b) #sum of two array
#concat array 
#vertical stacking
print(np.vstack((a,b)))
#Horizontal stacking
print(np.hstack((a,b)))
print(a.ravel()) #convert them into one array