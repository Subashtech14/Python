#*Multiple Inheritance
#It involves more than one parent class
class Parent:
    def func1(Self):
        print("Function1")
class Parent2:
    def func3(self):
        print("Function3")
class Child(Parent,Parent2):
    def func2(self):
        print("Function2")
ob=Child()
ob.func1()
ob.func3()