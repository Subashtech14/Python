#*single Inheritance
#when the inheritance involves one child class and one parent class
class Parent:
    def func1(Self):
        print("Function1")
class Child(Parent):
    def func2(self):
        print("Function2")
ob=Child()
ob.func1()