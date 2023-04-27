import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
#sin
y=np.sin(x)
plt.plot(x,y)
plt.show()
#cos
y=np.cos(x)
plt.plot(x,y)
plt.show()
#tan
y=np.tan(x)
plt.plot(x,y)
plt.show()
ar=np.array([1,2,3])
print(np.exp(ar))
print(np.log(ar))
print(np.log10(ar))