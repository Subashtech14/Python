#*Hirerachical Inheritance
#more than one type of inheritance
class Parent:
    def func1(Self):
        print("Function1")
class Parent2(Parent):
    def func3(self):
        print("Function3")
class Child(Parent):
    def func2(self):
        print("Function2")
ob=Child()
ob.func1()
ob1=Parent2()
ob1.func1()