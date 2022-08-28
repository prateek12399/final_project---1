from user_function import FoodFunction

class Foodmain:

    def __init__(self,foodfunction_obj):
        self.foodfunction_obj = foodfunction_obj

    def execute(self,choice):
        if choice == 1:
            print("***********Registration***********")
            self.foodfunction_obj.registration()

        elif choice == 2:
            print("***********Log in the applicaation**********")
            self.foodfunction_obj.log_in()
            
        elif choice == 3:
            print("***********Update Your Profile**********")
            self.foodfunction_obj.update_profile()
        
        else:
            print("***Invalid Input***")

if __name__ == "__main__":
    foodfunction_obj = FoodFunction()
    Foodmain = Foodmain(foodfunction_obj)                               

    while True:
        print("Enter \n1.Registration \n2.Log in the application \n3.Update Profile\n")
        choice = int(input("Enter your choice : "))
        Foodmain.execute(choice)