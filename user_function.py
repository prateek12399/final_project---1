from user import Food

class FoodFunction:
    foodlist = []
    foodlist1 = []    
    def registration(self):
        full_name = input("Enter your full name : ")
        phone_number = int(input("Enter your mo.no. :"))
        email = input("Enter your email :")
        address = input("Enter your address :")
        password = input("enter your password :")        
        food_obj = Food(full_name,phone_number,email,address,password)
        self.foodlist.append(food_obj)
        print("Registration Successfully")

    def log_in(self):
        while True:
            print("1.Place Your order")
            print("2.Order History")
            select = int(input("Select an Option :"))

            if select == 1:                       
                dict = {1:"Tandoori Chicken(4 piece)--->240",2:"Vegan burgur(1 piece)--->320rs",3:"Truffle Cake(500gm)--->900rs"}
                print(dict)
                size = int(input("How many item you want to select :"))
                dict1 ={}
                for i in range(size):
                    key = int(input("enter your number of item :"))
                    value = input("enter your  name of your item :")
                    dict1[key] = value
                print(dict1)
                print("****Your Order is Placed****")
                
            if select == 2:
                print("******Your Order History****")
                print(dict1)
            
    def update_profile(self):
        full_name = input("Enter your full name : ")
        phone_number = int(input("Enter your mo.no. :"))
        email = input("Enter your email :")
        address = input("Enter your address :")
        password = input("enter your password :")        
        food_obj = Food(full_name,phone_number,email,address,password)
        self.foodlist1.append(food_obj)
        print(" Prof1le Updated Successfully")