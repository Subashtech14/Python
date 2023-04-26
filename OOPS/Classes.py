#A Class is a blueprint from which specific objects are created
class Car():
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
    def price_inc(self):
        self.price=(self.price*1.5)
        print(self.price)
        
honda = Car('City',2017,10000)
tata = Car('Bolt',2016,1000000)
honda.cc=1500
honda.price_inc()
print(honda.__dict__) #TO View entire object using dict
print(tata.__dict__) 