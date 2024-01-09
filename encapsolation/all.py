from primary import Items
from add import Add

my_item = Items("Humayun", 500, 10) 
my_item.quantity = 599

def main(func):
    def inner(*args,**kwargs):
        print("Here is the infomation of -----")
        func(args,kwargs)
    return inner

def my_info (*args, **kwargs):
    for description in args:
        print(description, end= " ")
    print()    
    for dis,info in kwargs:
        print(f"{dis}:{info}",end= " ")
    print()    


my_info("Biography of Humayun",
        name = "Humayun",
        age = 24,
        occu = "Learner",
        aim = "Software"


        )        
