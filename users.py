# Customer
# Employee
# Admin

from abc import ABC
from orders import Order


class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        
class Customar(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()
        
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        # print(item.quantity)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded")
            else:
                # item.quantity = quantity
                self.cart.add_item(item, quantity)
                print("item added")
        else:
            print("Item not found") 
            
    def view_cart(self):
        print("************View Cart************")
        print("Name\tprice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")
    
    def pay_bill(self):
        total = self.cart.total_price
        print(f"Your total bill is: {total}")
        if total == 0:
            print("Your cart is empty. Nothing to pay.")
            return
        amount = int(input("Enter amount you want to pay: "))
        if amount < total:
            due = total - amount
            print(f"You paid {amount}. Still due: {due}")
        elif amount == total:
            print(f"Payment successful! You paid full {amount}.")
            self.cart.clear()
        else:
            extra = amount - total
            print(f"Payment successful! You paid {amount}. Extra balance: {extra} will be returned.")
            self.cart.clear()

    
class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary 

"""
!! Experiment !!
emp = Employee('Rohim', "rohim@gmail.com", 1524,"12 Dhaka","40", "Chef", 1200)
print(emp.age) 
!! ok !!
"""

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
    
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
    
    def view_employee(self, restaurent):
        restaurent.view_employee()
    
    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)
        
    def delete_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
    
    def view_manu(self, restaurent):
        restaurent.menu.show_menu()


"""
# !! Experiment !!
# add.add_employee("Sagor", "alom@gmail.com", 78624, "est nondipara, dhaka", 35, "Chef", 14000)
# add.view_employee()
# !! ok !!
mamar_r = Restaurent("Mamamr Halim and Restaurent")

mn = Menu()
item = FoodItem("pizza", 780, 12)
item1 = FoodItem("bargar", 480, 30)
add = Admin("Shah", "alam@gmail.com", 147829, "164/1 west dhaka")
add.add_new_item(mamar_r, item)
add.add_new_item(mamar_r, item1)
# mn.show_menu()

customar1 = Customar("Rohim", "ar@gmail.com", "0182546", "164/a East bazart")
customar1.view_menu(mamar_r)

item_name = input("Enter Item Name : ")
item_quantity = int(input("Enter Item Quantity : "))

customar1.add_to_cart(mamar_r, item_name, item_quantity)
customar1.view_cart()
"""
