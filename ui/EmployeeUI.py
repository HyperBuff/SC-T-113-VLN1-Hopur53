import math



from logic.MainLogic import MainLogic
from models.Employee import Employee

from ui.PrinterUI import PrinterUI

class EmployeeUI:

    def __init__(self):
        self.items_per_page = 10
        self.logic = MainLogic()
        self.printer = PrinterUI()
        self.success_msg = ""
        self.warning_msg = ""

    # Prints out employee's menu
    def menu(self):
        while True:
            self.printer.header("Employees Menu")
            self.printer.print_options(['Create an employee', 'View employees'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == '1':
                if self.create():
                    self.success_msg = "New employee has been created"
                    self.view()
            elif action == '2':
                self.view()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    # Prints out all employee
    def view(self, current_page = 1):

        while True:   
            employees = self.logic.get_all_employees()
            employees_count = len(employees)
            last_page = math.ceil(employees_count / self.items_per_page)
            self.printer.header("View employees")
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else employees_count
            self.print_employees(employees, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(N)ext page / (P)revious page / (S)elect employee: ").lower()
            if action == 'q':
                break
            elif action == 'n' or action == "next":
                if current_page >= last_page:
                    current_page = last_page
                    self.warning_msg = "You are currenly on the last page"
                else:
                    current_page += 1
            elif action == 'p' or action == "previous":
                if current_page > 1:
                    current_page -= 1
                else:
                    current_page = 1
                    self.warning_msg = "You are currenly on the first page"
            elif action == 's' or action == "select":
                employee_id = input("Select employee by ID: ")
                employee = self.logic.get_employee_by_id(employee_id)
                if employee is None:
                    self.warning_msg = "Employee not found"
                else:
                    self.select_employee(employee_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single employee
    def select_employee(self, employee_id):
        while True:
            employee = self.logic.get_employee_by_id(employee_id)
            self.printer.header("View employee")
            print("ID:\t\t\t\t{}\nRole:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\n".format(employee_id, employee.role, employee.name, employee.email, employee.ssn, employee.phone, employee.homephone, employee.address, employee.postal))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(employee_id)
            elif action == 'd' or action == 'delete':
                if self.delete(employee_id):
                    self.success_msg = "Employee has been deleted"
            else:
                self.warning_msg = "Please select available option"
            
    # Prints out table of employee
    def print_employees(self, employees, start, end, current_page, last_page):
        print("|{:^6}|{:^15}|{:^30}|{:^40}|{:^30}|{:^20}|{:^20}|{:^30}|{:^15}|".format("ID", "Role", "Name", "Email", "Social security number", "Mobile phone", "Home phone", "Address", "Postal code"))
        print('-' * 216)
        for i in range(start, end):
            print("|{:^6}|{:<15}|{:<30}|{:<40}|{:<30}|{:<20}|{:<20}|{:<30}|{:<15}|".format(employees[i].id, employees[i].role, employees[i].name, employees[i].email, employees[i].ssn, employees[i].phone, employees[i].homephone, employees[i].address, employees[i].postal))
        print("{:^216}".format("Page {} of {}".format(current_page, last_page)))
        self.printer.new_line()

    # Create employee
    def create(self):
        self.printer.header("Add employee")
        role = None
        self.printer.new_line()
        self.printer.print_fail("Press q to go back")
        self.printer.new_line()
        while role == None:
            role = self.select_role()
            if role == 'q':
                return    
        self.printer.new_line()
        print("Enter employee details:")
        while True:
            name = input("\tEnter name: ")
            if name == 'q':
                return
            if len(name) < 1:
                self.printer.print_warning("Name must been at least 1 character")
            else:
                break
        while True:
            email = input("\tEnter email: ")
            if email == 'q':
                return
            if len(email) < 1:
                self.printer.print_warning("Email must been at least 1 character")
            elif not self.logic.is_email_valid(email):
                self.printer.print_warning("Email is not valid")
            else:
                break
        while True:
            ssn = input("\tEnter social security number: ")
            if ssn == 'q':
                return
            if len(ssn) < 1:
                self.printer.print_warning("Social security number must been at least 1 character")
            elif not self.logic.is_ssn_valid(ssn):
                self.printer.print_warning("Social security number is not valid")
            else:
                break
        while True:
            phone = input("\tEnter mobile phone: ")
            if phone == 'q':
                return
            if len(phone) < 1:
                self.printer.print_warning("Mobile phone must been at least 1 character")
            elif not self.logic.is_phone_number_valid(phone):
                self.printer.print_warning("Phone number is not valid")
            else:
                break
        while True:
            homephone = input("\tEnter home phone: ")
            if homephone == 'q':
                return
            if len(homephone) < 1:
                self.printer.print_warning("Home phone must been at least 1 character")
            elif not self.logic.is_phone_number_valid(phone):
                self.printer.print_warning("Phone number is not valid")
            else:
                break
        while True:
            address = input("\tEnter address: ")
            if address == 'q':
                return
            if len(address) < 1:
                self.printer.print_warning("Address must been at least 1 character")
            else:
                break
        while True:
            postal = input("\tEnter postal: ")
            if postal == 'q':
                return
            if len(postal) < 1:
                self.printer.print_warning("Postal must been at least 1 character")
            else:
                break
        new_employee = Employee(role, name, address, postal, ssn, phone, homephone, email)
        self.logic.create_employee(new_employee) 
        return True         
 
    # Edit employee
    def edit(self, id):
        while True:
            updates = {}
            self.printer.header("Edit employee")
            self.printer.print_options(['Change role', 'Change email', 'Change mobile phone', 'Change home phone', 'Edit address', 'Edit postal code'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == 'q':
                break
            if action == '1':
                role = None
                while role == None:
                    role = self.select_role()
                if role == 'q':
                    break    
                updates["role"] = role
            elif action == '2':
                while True:
                    email = input("\tEnter email: ")
                    if email == 'q':
                        break
                    if len(email) < 1:
                        self.printer.print_warning("Email must been at least 1 character")
                    elif not self.logic.is_email_valid(email):
                        self.printer.print_warning("Email is not valid")
                    else:
                        updates["email"] = email
                        break
            elif action == '3':
                while True:
                    phone = input("\tEnter mobile phone: ")
                    if phone == 'q':
                        break
                    if len(phone) < 1:
                        self.printer.print_warning("Mobile phone must been at least 1 character")
                    elif not self.logic.is_phone_number_valid(phone):
                        self.printer.print_warning("Phone number is not valid")
                    else:
                        updates["phone"] = phone
                        break
            elif action == '4':
                while True:
                    phone = input("\tEnter home phone: ")
                    if phone == 'q':
                        break
                    if len(phone) < 1:
                        self.printer.print_warning("Mobile phone must been at least 1 character")
                    elif not self.logic.is_phone_number_valid(phone):
                        self.printer.print_warning("Phone number is not valid")
                    else:
                        updates["homephone"] = phone
                        break
            elif action == '5':
                while True:
                    address = input("\tEnter address: ")
                    if address == 'q':
                        break
                    if len(address) < 1:
                        self.printer.print_warning("Address must been at least 1 character")
                    else:
                        updates["address"] = address
                        break
            elif action == '6':
                while True:
                    postal = input("\tEnter postal: ")
                    if postal == 'q':
                        return
                    if len(postal) < 1:
                        self.printer.print_warning("Postal must been at least 1 character")
                    else:
                        updates["postal"] = postal
                        break
            self.logic.update_employee(id, updates)

            keys = list(updates.keys())

            if(len(keys) > 0):
                col = keys[0]
                self.success_msg = "{} has been modified".format(col.capitalize())

    # Delete employee
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this employee? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_employee(id)
            return True
        return False

    # Select available roles
    def select_role(self):
        print("Select role for employee:\n\t1. Admin\n\t2. Delivery\n\t3. Booking\n\t4. Mechanic\n\t5. Financial")
        action = input("\nChoose an option: ")
        if action == 'q':
            return 'q'
        elif action == str(1):
            return "Admin"  
        elif action == str(2):
            return "Delivery"
        elif action == str(3):
            return "Booking"
        elif action == str(4):
            return "Mechanic"
        elif action == str(5):
            return "Financial"
        else:
            self.printer.print_warning("Please select available option")
            self.printer.new_line()
            return None

    # Outputs warnings and success messages
    def print_msg(self):
        if not self.warning_msg == "":
            self.printer.print_warning(self.warning_msg)
            self.warning_msg = ""
        elif not self.success_msg == "":
            self.printer.print_success(self.success_msg)
            self.success_msg = ""
        else:
            self.printer.new_line()
