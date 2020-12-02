from logic.MainLogic import MainLogic
from models.Employee import Employee

class EmployeeUI:

    def __init__(self):
        self.user_id = None

        self.logic = MainLogic()

    def menu(self):
        print("\n\n1. Add an employee\n2. List all employess\n3. Edit employee\n4. Remove employee\n\nPress q to go back")
        action = input("\nChoose an option: ").lower()

        if action == str(1):
            self.create()
        elif action == str(2):
            self.read()
        elif action == str(3):
            self.update()
        elif action == str(4):
            self.delete()
        elif action == 'q':
            return

    def create(self):
        self.header("Add employee")
        print("Enter employee details:")
        
        name = input("\tEnter name: ")
        address = input("\tEnter address: ")
        postal = input("\tEnter postal: ")
        ssn = input("\tEnter ssn: ")
        phone = input("\tEnter mobile phone: ")
        homephone = input("\tEnter homephone: ")
        email = input("\tEnter email: ")
        role = input("\tRole")

        new_employee = Employee(role, name, address, postal, ssn, phone, homephone, email)
        self.logic.create_employee(new_employee)          


    def read(self):
        pass

    def update(self):
        pass

    def delete(self):  
        pass

    
    def header(self, title):
        print("-" * 50)
        print("|{:^48}|".format(title))
        print("-" * 50)
        print()