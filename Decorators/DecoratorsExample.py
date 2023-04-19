#Decorators
#Decorators in python are very powerful which modify the behavior of a function without modifying it permanenently.
#It basically wraps another function and since both functions are callable,it returns callable;
def function1(function):
    def wrapper():
        print("Hello")
        function()
        print("Welcome to Python Edureka tutorial ")
    return wrapper
@function1 #pysyntax
def function2():
    print("Pythonista")
function2()
#or 
# function2=function1(function2)
# function2()
def E1function1(function):
    def wrapper(*args, **kwargs):
        print("Hello")
        function(*args,**kwargs)
        print("Welcome to edureka python tutorial")
    return wrapper
@E1function1
def E1function2(name):
    print(f"{name}")
E1function2("Subash")