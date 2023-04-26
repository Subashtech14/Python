#Method Overriding can be achieved to change functionality of parent class function
class Parent:
    def function(self):
        print("This is Function1")
class child(Parent):
    def function(Self):
        print("This is function 2")
ob=child()
ob.function()
