class CreateItem:

    def __init__(self,quantity):
        # self.price=price
        self.quantity=quantity
    
    def __add__(self,quantity):
        return CreateItem(self.quantity+quantity)
        
    def __mul__(self,price):
        return self.quantity*price
    

objc=CreateItem(50)
new_inventory=objc+50

print(new_inventory*5)
        