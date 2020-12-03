import math

from logic.MainLogic import MainLogic
from models.Employee import Employee

class EmployeeUI:

    def __init__(self):
        self.logic = MainLogic()

    def menu(self):
        action = ''
        while not action == 'q':
            print("\n\n1. Add an employee\n2. List all employess\n3. Edit employee\n4. Remove employee\n\n\33[;31mPress q to go back\33[;0m\n")
            action = input("\nChoose an option: ").lower()

            if action == str(1):
                self.create()
            elif action == str(2):
                self.read()
            elif action == str(3):
                self.update()
            elif action == str(4):
                self.delete()

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
        role = rolechoose()

        new_employee = Employee(role, name, address, postal, ssn, phone, homephone, email)
        return self.logic.create_employee(new_employee)          


    def read(self):
        self.header("All employees")

        employees = self.logic.get_all_employees()

        page = 1
        start = 0 

        while True:

            last_page = math.ceil(len(employees) / 10)

            print(f"{page}")

            if page > 1:
                start = 10 * (page-1)
            if len(employees) < (start + 10):
                end = len(employees)
            else:   
                end = start + 10

            print("\n|{:^10}|{:^30}|{:^20}|{:^20}|{:^30}|{:^20}|{:^20}|{:^30}|{:^20}|".format("ID", "Name", "Address", "Postal code", "Social security number", "Mobilephone", "Homephone", "E-mail", "Role"))
            print('-' * 210)
            for i in range(start, end):
                print("|{:^10}|{:<30}|{:<20}|{:<20}|{:<30}|{:<20}|{:<20}|{:<30}|{:<20}|".format(employees[i].id, employees[i].name, employees[i].address, employees[i].postal, employees[i].ssn, employees[i].phone, employees[i].homephone, employees[i].email, employees[i].role))

            action = input("Next page / Previous page (N/P): \nPress q to go back").lower()

            if action == "n":
                if last_page > page:
                    page += 1
            elif action == "p":
                if page > 1:
                    page -= 1
            elif action == "q":
                break


    def update(self):
        self.header("Edit employees")
        self.read()
        id = input("\tEnter id: ")

        choice = ""
        updates = {}
        while choice != "q":
            print("\n1. Edit name\n2. Edit address\n3. Edit postal\n4. Edit phone\n5. Edit homephone\n"
                                      "6. Edit email\n7. Edit role\n\n\33[;31mPress q to save\33[;0m\n")
            choice = input("Enter your choice: ").lower()
            if choice == "1":
                name = input("Enter name: ")
                updates["name"] = name
            elif choice == "2":
                address = input("Enter address: ")
                updates["address"] = address
            elif choice == "3":
                postal = input("Enter postal code")
                updates["postal"] = postal
            elif choice == "4":
                phone = input("Enter phone: ")
                updates["phone"] = phone
            elif choice == "5":
                homephone = input("Enter homephone: ")
                updates["homephone"] = homephone
            elif choice == "6":
                email = input("Enter email: ")
                updates["email"] = email
            elif choice == "7":
                role = input("Enter role: ")
                updates["role"] = role

        #tekur inn id fyrir employee
        #tekur inn dict af uppfærslum
        self.logic.update_employee(id, updates)

    def delete(self):  
        #tekur inn id fyrir employee
        id = input("\tEnter id: ")
        return self.logic.delete_employee(id)

    
    def header(self, title):
        print("-" * 50)
        print("|{:^48}|".format(title))
        print("-" * 50)
        print()


def rolechoose():
    print("1. Admin, 2. Delivery, 3. Booking, 4. Mechanic, 5. Financial")
    userinput = input("Choose Role: ")
    if userinput == "1":
        return "Admin"  
    elif userinput == "2":
        return "Delivery"
    elif userinput == "3":
        return "Booking"
    elif userinput == "4":
        return "Mechanic"
    elif userinput == "5":
        return "Financial"
    else:
        print("Choose a number to choose a role")