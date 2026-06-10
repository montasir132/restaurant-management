```markdown
# 🍽️ Restaurant Management System (Python)

A simple **Restaurant Management System** built with Python OOP concepts.  
This project demonstrates how to manage customers, admins, employees, menus, and orders in a restaurant environment.

---

## 📌 Features

### 👨‍🍳 Admin Interface
- Add new food items to the menu
- Add new employees
- View employee list
- View menu items
- Delete items from the menu

### 🛒 Customer Interface
- View menu
- Add items to cart
- View cart with total price
- Pay bill (customizable: partial payment, full payment, or extra payment)
- Exit system

---

## 🏗️ Project Structure

```
├── main.py          # Entry point of the program
├── food_item.py     # FoodItem class (name, price, quantity)
├── menu.py          # Menu class (add, find, remove, show items)
├── orders.py        # Order class (cart management, total price, clear cart)
├── restaurent.py    # Restaurent class (employees, menu)
├── users.py         # User, Customer, Employee, Admin classes
```

---

## ⚙️ Installation & Run

1. Clone the repository:
   ```bash
   git clone https://github.com/montasir132/restaurant-management.git
   cd restaurant-management
   ```

2. Run the program:
   ```bash
   python main.py
   ```

---

## 🎯 How It Works

- **Admin** logs in → can add/view/delete menu items and manage employees.  
- **Customer** logs in → can browse menu, add items to cart, view cart, and pay bill.  
- **PayBill** option allows:
  - Partial payment (shows due amount)
  - Full payment (clears cart)
  - Extra payment (shows balance to return)

---

## 🛠️ Technologies Used
- Python 3.x
- Object-Oriented Programming (OOP)

---

## 🚀 Future Improvements
- Add database support (SQLite/MySQL) instead of in-memory lists
- Add authentication system for Admin/Customer
- GUI interface using Tkinter or PyQt
- Online payment gateway integration
