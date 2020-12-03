import math

from logic.MainLogic import MainLogic
from models.Employee import Employee

class EmployeeUI:

    def __init__(self):
        self.items_per_page = 10
        self.logic = MainLogic()


    # Employee Menu

    def menu(self):

        while True:
            self.header("Employees Menu")
            print("\n\n1. Create an employee\n2. View employees\n\n\33[;31mPress q to go back\33[;0m\n")
            action = input("Choose an option: ").lower()

            if action == str(1):
                self.create()
            elif action == str(2):
                self.view()
            elif action == 'q':
                break

    # View Employees
    
    def view(self, current_page = 1):

        while True:   
            self.header("View employees")

            employees = self.logic.get_all_employees()
            employees_count = len(employees)

            last_page = math.ceil(employees_count / self.items_per_page)

            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else employees_count


            self.print_employees(employees, start, end)

            action = input("\n(N)ext page / (P)revious page / (S)elect employee / (Q)uit (N/P/S/Q): ").lower()

            if action == 'q':
                break
            elif action == 'n':
                if current_page >= last_page:
                    current_page = last_page
                    print("You are currenly on the last page")
                else:
                    current_page += 1
            elif action == 'p':
                if current_page > 1:
                    current_page -= 1
                else:
                    current_page = 1
                    print("You are currenly on the first page")
            elif action == 's':
                employee_id = input("Select employee by id: ")
                self.select_employee(employee_id)



    def select_employee(self, id):
        
        while True:

            self.header("View employee")

            employee = self.logic.get_employee_by_id(id)

            if employee is None:
                print("Employee with id: {} wasn't found".format(id))
                return

            print("ID:\t\t\t\t{}\nName:\t\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nE-mail:\t\t\t\t{}\nRole:\t\t\t\t{}\n".format(id, employee.name, employee.address, employee.postal, employee.ssn, employee.phone, employee.homephone, employee.email, employee.role))

            action = input("\n(E)dit / (D)elete / (Q)uit (E/D/Q): ").lower()

            if action == 'q':
                break
            elif action == 'e':
                self.edit(id)
            elif action == 'd':
                self.delete(id)
                break

    def print_employees(self, employees, start, end):
        print("\n|{:^10}|{:^30}|{:^25}|{:^20}|{:^30}|{:^20}|{:^20}|{:^30}|{:^20}|".format("ID", "Name", "Address", "Postal code", "Social security number", "Mobile phone", "Home phone", "E-mail", "Role"))
        print('-' * 210)
        for i in range(start, end):
            print("|{:^10}|{:<30}|{:<25}|{:<20}|{:<30}|{:<20}|{:<20}|{:<30}|{:<20}|".format(employees[i].id, employees[i].name, employees[i].address, employees[i].postal, employees[i].ssn, employees[i].phone, employees[i].homephone, employees[i].email, employees[i].role))


    def create(self):
        self.header("Create employee")
        role = None
        print("\33[;31mPress q to go back\33[;0m\n")

        while role == None:
            role = self.select_role()
            if role == 'q':
                return

        print("\nEnter employee details:")
        name = input("\tEnter name: ")
        if name == 'q':
            return
        email = input("\tEnter email: ")
        if name == 'q':
            return
        address = input("\tEnter address: ")
        if name == 'q':
            return
        postal = input("\tEnter postal: ")
        if name == 'q':
            return
        ssn = input("\tEnter ssn: ")
        if name == 'q':
            return
        phone = input("\tEnter mobile phone: ")
        if name == 'q':
            return
        homephone = input("\tEnter homephone: ")
        if name == 'q':
            return

        new_employee = Employee(role, name, address, postal, ssn, phone, homephone, email)
        return self.logic.create_employee(new_employee)          


  
    def edit(self, id):
        self.header("Edit employee")

        updates = {}
        while True:
            print("1. Edit name\n2. Edit address\n3. Edit postal\n4. Edit phone\n5. Edit homephone\n6. Edit email\n7. Edit role\n\n\33[;31mPress q to go back\33[;0m\n")
            action = input("Choose an option: ").lower()

            if action == 'q':
                break

            new_value = input("Change to: ")

            if action == str(1):
                updates["name"] = new_value
            elif action == str(2):
                updates["address"] = new_value
            elif action == str(3):
                updates["postal"] = new_value
            elif action == str(4):
                updates["phone"] = new_value
            elif action == str(5):
                updates["homephone"] = new_value
            elif action == str(6):
                updates["email"] = new_value
            elif action == str(7):
                updates["role"] = new_value
            self.logic.update_employee(id, updates)

    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this employee? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_employee(id)
    
    def header(self, title):
        print("-" * 50)
        print("|{:^48}|".format(title))
        print("-" * 50)
        print()


    def select_role(self):
        print("Select role for employee:\n\t1. Admin\n\t2. Delivery\n\t3. Booking\n\t4. Mechanic\n\t5. Financial")
        action = input("\nChoose an option: ")
        if action == 'q':
            return 'q'
        elif action == "1":
            return "Admin"  
        elif action == "2":
            return "Delivery"
        elif action == "3":
            return "Booking"
        elif action == "4":
            return "Mechanic"
        elif action == "5":
            return "Financial"
        else:
            print("\n\33[;31mRole wasn't fount, please try again.\33[;0m\n")
            return None


# Input Validation 

"""
def checkemail(id, email):
    email_list = email.split("@")
    if len(email_list) == 2:
        new_list = email_list[1].split(".")
        final_list = []
        final_list.append(email_list[0])
        final_list.append(new_list[0])
        final_list.append(new_list[1])
        if len(final_list[0]) >= 1 and len(final_list[1]) >= 1 and len(final_list[2]) >= 2:
            return True
        else:
            return None 
    else:
        return None


def checkssn(ssn):
    int_list = []
    for number in ssn:
        try:
            if number != "-":
                int_ssn = int(number)
                int_list.append(int_ssn) 
        except ValueError:
            return None
    if len(int_list) == 10:
        return True
    else: 
        return None
"""