from main import Items


class Add(Items):
    all_items= []
    def __init__(self, name, price, quantity,broken_phone=0):
        super().__init__(name, price, quantity)
        self.broken_phone =  broken_phone
        Add.all_items.append(self)

        assert self.price >=1, f"{self.price} is more than of equal One"
        assert self.quantity >= 1,f"{self.quantity} is more than of equal One"
        assert self.broken_phone >= 1,f"{self.broken_phone} is more than of equal One"
print("-------------------------------")        
print("Here I added new items by using super method")  
print()      
new1 =Add("Keyboard", 2000, 30,5)
new1.total_price()        
new1.average_price() 
print("-------------------------------")   

print("Here I added new items by using super method")  
print() 
new_all_items = Add.all_items
print(new_all_items)
new1.total_price() 
new1.average_price()




