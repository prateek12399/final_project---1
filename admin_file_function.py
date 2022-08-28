import imp
from admin import food

class foodfunction:
    foodlist =  []
    def add_food(self):
        FoodID   = int(input("Enter Your Food ID :"))
        Name     = input("Enter Your Food Name:")
        Quantity = int(input("Enter Your Food Quantity :"))
        Price    = float(input("Enter Your Food Price :"))
        Discount = int(input("Enter Your Food Discount :"))
        Stock    = int(input("Enter Your Food Stock :"))
        food_obj = food(FoodID,Name,Quantity,Price,Discount,Stock)
        self.foodlist.append(food_obj)
        print("Food Successfully Added")

    def view_food(self):
        for  i in self.foodlist:
            print(i)

    def edit_food(self):
        FoodID = int(input("enter your food id :"))
        for j in self.foodlist:
            if j.FoodID == FoodID :
                Name     = input("Enter Your Food Name:")
                Quantity = int(input("Enter Your Food Quantity :"))
                Price    = float(input("Enter Your Food Price :"))
                Discount = int(input("Enter Your Food Discount :"))
                Stock    = int(input("Enter Your Food Stock :"))

                j.set_Name(Name)
                j.set_Quantity(Quantity)
                j.set_Price(Price)
                j.set_Discount(Discount)
                j.set_Stock(Stock)
                
                print("successfully food Edited")
                break
            else:
                print("no food found")
         

    def remove_food(self):
        FoodID = int(input("Enter your Food ID :"))
        for j in self.foodlist:
            if self.FoodID == FoodID :
                self.foodlist.remove(j)
                print("Successfuly Food Deleted")
                break
            else:
                print("Food not found")
