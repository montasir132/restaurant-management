from menu import Menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # eta hocche database
        self.menu = Menu()
        
    def add_employee(self, employee):
        #  employee class ar object
        # employee = Employee(employee)
        self.employees.append(employee)
        
    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)
