#Generators(return elements one by one)
#They area function that return traversable objects.
#Produce items one at a time and only when required. They are run along with for loops.
#Advantages of using generators
#1 Easy to use 2 Better Memory management and utilization 3 can be used to produce inifinte items
#4 it can be used to pipline a number of operations
def new(dict):
    for x,y in dict.items():
        yield x,y
a={1:"Hi",2:"Welcome"}
b=new(a)
print(b)
print(next(b))
print(next(b))

def myfunc(i):
    while (i <= 3):
        yield i
        i+=1
j=myfunc(2)
print(next(j))

#Print square
def ex():
    n=3
    yield n
    n=n*n
    yield n
v=ex()
for x in v:
    print(x)

#Generator Expression
f=range(6)
print("List comp",end=":")
a=[ x+2 for x in f]
print(a)
print("gen exp",end=":")
r=(x+2 for x in f)
print(r)
for x in r:
    print(x)
