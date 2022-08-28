class Food:

    def __init__(self,full_name,phone_number,email,address,password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        

    def __str__(self):
        return f"Full Name : {self.full_name} \nPhone Number : {self.phone_number} \nEmail : {self.email} \nPassword : {self.password} \nAddress : {self.address}"


    def set_full_name(self,full_name):
        self.full_name = full_name

    def get_full_name(self):
        return self.full_name

    def set_phone_number(self,phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def set_email(self,email):
        self.email = email

    def get_email(self):
        return self.email

    def set_addresss(self,address):
        self.address= address

    def get_address(self):
        return self.address
            
    def set_password(self,password):
        self.password = password

    def get_password(self):
        return self.password
