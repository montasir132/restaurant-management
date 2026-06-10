from food_item import FoodItem
from menu import Menu
from users import Customar, Admin, Employee
from restaurent import Restaurent
from orders import Order

mamar_res = Restaurent("Star Residence")


# Customer Interface
def customar_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    customar = Customar(name = name, email = email, phone = phone, address = address)
    
    while True:
        print(f"Welcome {customar.name}!!")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            customar.view_menu(mamar_res)
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))
            customar.add_to_cart(mamar_res, item_name, item_quantity)
        elif choice == 3:
            customar.view_cart()
        elif choice == 4:
            customar.pay_bill()
        elif choice == 5:
            break
        else:
            print(f"Invalid Your Choice : {choice}.")


# Admin Interface
def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    admin = Admin(name = name, email = email, phone = phone, address = address)
    
    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New employee")
        print("3. View employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            item_name = input("Enter Item name : ")
            item_price = int(input("Enter Item price : "))
            item_quantity = int(input("Enter Item quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_res, item)
        elif choice == 2:
            name = input("Enter Employee Name : ")
            email = input("Enter Employee Email : ")
            phone = input("Enter Employee Phone : ")
            address = input("Enter Employee Address : ")
            age = input("Enter Employee Age : ")
            designation = input("Enter Employee Designation : ")
            salary = input("Enter Employee Salary : ")
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(mamar_res, employee)
        elif choice == 3:
            admin.view_employee(mamar_res)
        elif choice == 4:
            admin.view_manu(mamar_res)
        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.delete_item(mamar_res, item_name)
        elif choice == 6:
            break
        else:
            print(f"Invalid Your Choice : {choice}.")
            
while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        customar_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print(f"Invalid Your Choice : {choice}.")
        