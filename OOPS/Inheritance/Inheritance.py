#Inheritance
#A class can inherit attributes and behavior methods from another class called superclass.
#A class which inherits from a super class is called a subclass,also called heir class or child class.
class Car():
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
    def price_inc(self):
        self.price=(self.price*1.5)
        print(self.price)
class SupperCar(Car):
    def __init__(self,modelname,yearm,price,cc):
        super.__init__(odelname,yearm,price) #refering back to the parent init constructor
        self.cc=cc

honda = SupperCar('City',2017,10000)
tata = SupperCar('Bolt',2016,1000000)
honda.cc=1500
honda.price_inc()
# print(help(honda))
print(honda.yearm)
#init()
#__init__() function is called automatically every time the class is used to create an object.
class Parent:
    def __init__(self,fname,fage):
        self.name=fname
        self.age=fage
    def view(self):
        print(self.__dict__)
class child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self,fname, fage)
        self.lastname="Subash"
    def view(self):
        print(self.age,self.lastname,self.name)
ob=child(27, 'Devil')
ob.view()