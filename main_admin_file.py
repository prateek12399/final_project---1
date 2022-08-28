from admin_function import  foodfunction

class foodmain:

    def __init__(self,foodfunction_obj):
        self.foodfunction = foodfunction_obj

    def executed(self,choice):
        if choice == 1 :
            print("***ADD FOOD***")        
            self.foodfunction.add_food()

        if choice == 2 :
            print("***VIEW FOOD***")        
            self.foodfunction.view_food()

        if choice == 3 :
            print("***EDIT FOOD***")        
            self.foodfunction.edit_food()

        if choice == 4 :
            print("***REMOVE FOOD***")        
            self.foodfunction.remove_food()


if __name__ =='__main__':
    foodfunction_obj = foodfunction()
    foodmain =  foodmain(foodfunction_obj)

    while True:
        print("Enter \n1.Add Food \n2.View Food \n3.Edit Food \n4.Remove Food")
        choice = int(input("enter your choice :"))
        foodmain.executed(choice)
