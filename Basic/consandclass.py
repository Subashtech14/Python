class Item:
    def __init__(self,name:str,price:int,quantity=0):
        # print(f"I AM CREATED {name}")
        #Run validation to the received arguments and throws error
        assert price >= 0 ,f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0,f"quantity {quantity} is not greater than or equal to zero"
        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
        pass
    def calculate_total_price(self):
        return self.price * self.quantity
        
    # pass is used as a placeholder for future code
    
item1 = Item("kilp",100)
# item1.name="Subash"
# item1.price= 100
# item1.quantity =5

print(item1.calculate_total_price())
item2 = Item("killls",100,60)
# item2.name="Laptop"
# item2.price= 100
# item2.quantity =6
print(item2.calculate_total_price())
