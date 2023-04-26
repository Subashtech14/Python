#Super
#Super function directly calls the parent class method.
class Parent:
    def function(self):
        print("This is Function1")
class child(Parent):
    def function2(Self):
        super().function()
        print("This is function 2")
ob=child()
ob.function2()
