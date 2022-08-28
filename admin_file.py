class food:
    def  __init__(self,FoodID,Name,Quantity,Price,Discount,Stock):
        self.FoodID   = FoodID
        self.Name     = Name
        self.Quantity = Quantity
        self.Price    = Price
        self.Discout  = Discount
        self.Stock    = Stock

    def __str__(self):
        return f"Food ID : {self.FoodID} \nName : {self.Name} \nQuantity : {self.Quantity} \nPrice :{self.Quantity} \nPrice : {self.Price} \nDiscount :{self.Discout} \nStock : {self.Stock}"

    def set_FoodID(self,FoodID):
        self.FoodID = FoodID

    def get_FoodID(self):
        return self.FoodID

    def set_Name(self,Name):
        self.Name = Name

    def get_Name(self):
        return self.Name

    def set_Quantity(self,Quantity):
        self.Quantity = Quantity

    def get_Quantity(self):
        return self.Quantity

    def set_Price(self,Price):
        self.Price = Price

    def get_Price(self):
        return self.Price

    def set_Discount(self,Discount):
        self.Discount = Discount

    def get_Discount(self):
        return self.Discount

    def set_Stock(self,Stock):
        self.Stock = Stock

    def get_Stock(self):
        return self.Stock



