#Encapsulation
#Binding the data and code together as a single unit
#Securing data by hiding the implementation details to user
#By using getter and setter and @project
#Abstraction
#Hides the implementation details and only provides the functionality to the user
#We can achieve abstraction using Abstract classes and Interfaces
#Abstract class cant have objects
from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def price_inc(self):
        pass
class SupperCar(Car):
    def __init__(self,modelname,yearm,price,cc):
        # super.__init__(odelname,yearm,price) #refering back to the parent init constructor
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
        self.cc=cc
        
    def price_inc(self):
        self.price=(self.price*1.5)
        print(self.price)
        

honda = SupperCar('City',2017,10000,100)
tata = SupperCar('Bolt',2016,1000000,100)

honda.price_inc()
# print(help(honda))
print(honda.yearm)