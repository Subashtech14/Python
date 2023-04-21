#Use Cases
#Fibonacci series
def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x>50:
        break
    print(x,end=" ")
#Number stream
a=range(1,100,2)
b=(x for x in a)
print(b)
for y in b:
    print(y)
#sinewave using normal function
# import numpy as np
# from matplotlib import pyplot as pit
# import seaborn as sb
# def s(flip = 2):
#     x=np.linspace(1,4,100)
#     for i in range(1,5):
#         pit.plot(x,np.sin(x+i*.5)*(7-i)*flip)
# sb.set()
# s()
# pit.show()
#sinewave using generator function
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def S(flip = 2):
    x=np.linspace(0,14,100)
    for i in range(1,10):
        yield(plt.plot(x,np.sin(x+i*.5)*(7-i)*flip))
sb.set()
s=S()
plt.show()
print(next(s))
print(next(s))