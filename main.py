import os
import csv 
class Items:
    all_items = []
    def __init__(self,name,price,quantity):
        # Assign to obejes
        self.name = name
        self.price = price
        self.quantity = quantity
        Items.all_items.append(self)
        # To set a condition for each paramiter by assert
        assert self.price >=1, f"{self.price} is more than of equal One"
        assert self.quantity >= 1,f"{self.quantity} is more than of equal One"
    def info(self):  
        print(f"The {self.name} each price is {self.price} and I need to {self.quantity}")
    def total_price(self):
        total = self.price * self.quantity
        print(f"Your total {self.name} price is {total} TK")
    def average_price (self):
        average = (self.price * self.quantity)/ self.quantity  
        print(f"Your average price each {self.name} is {average} TK")  
    @classmethod    
    def import_csv(cls):
        script_path = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_path, 'items.csv')

        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        created_items = []    

        for item in items:
            name_str = item.get('name')
            price_str = item.get('price')
            quantity_str =item.get('quantity')
            if name_str is not None and price_str is not None and quantity_str is not None:
                try:
                    name = str(name_str)
                    price = float(price_str)
                    quantity = int(quantity_str)

                    created = Items(
                        name =name,
                        price = price,
                        quantity = quantity
                    ) 
                    created_items.append(created)

                except ValueError as e :
                    print(f"Error is here {name}: {e}")
        return created_items   
    @staticmethod
    def is_integer (num):
        if isinstance (num, int):
            return True 
        elif isinstance(num, float):
            return False
        else:
            return False
        
                






    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"    


item1 = Items("Mobile", 12344, 20)
item2 = Items("Computer", 30000, 10)
item3= Items("Laptop", 50000, 5)
item4 = Items("LED TV", 60000, 2)

print("Below the simple method to get all items from class")
get_all_iteams = Items.all_items
print("Got all items by using simple" ,get_all_iteams) 
print()
print("Below the import csv file to get all items from class by using ClassicMethod ")
get_all_iteams_csv = Items.import_csv()
print(f"Got all items by using CSV file: {get_all_iteams_csv}") 

print()
print("Check Is_integer by using staic method")
is_integer = Items.is_integer(7)
print(is_integer)

           