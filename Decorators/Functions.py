#Functions in python
#First-Class Object : In python,everything is treated as an object including all the data types,
#functions too. Therfore, a function is also known as a first-class object and can be passed around as arguments.
#Inner-functions: it is possible to define functions inside a function. That functin is called as inner function.
#First-Class function
def func1(name):
    return f"Hello  {name}"
def func2(name):
    return f"{name} , how you doing?"
def func3(func4):
    return func4('Dear Learner')
print(func3(func1))
print(func3(func2))
#Inner Function
def func():
    print("first function")
    def func6():
        print("first child function")
    def func7():
        print("Second Child function")
    func6()
    func7()
func()
#Returning a Function
def rfunc(n):
    def rfunc1():
        return "Edureka"
    def rfunc2():
        return "Python"
    if(n==1):
        return rfunc1
    else:
        return rfunc2
a=rfunc(1)
b=rfunc(2)
print(a())
print(b())