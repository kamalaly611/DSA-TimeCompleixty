class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address  # Address instance

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)

    def info(self):
        return f"Name: {self.name}, Gender: {self.gender}, Address: {self.address.city}, {self.address.pincode}, {self.address.state}"


class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state
    

add=Address('Gahkuch',1234,'GB')
cust=Customer('Kamal','Male',add)
print(cust.address.state)

cust.edit_profile('Mishal','Yasin',9876,'Gupis')
print(cust.address.pincode)
print(cust.info())  