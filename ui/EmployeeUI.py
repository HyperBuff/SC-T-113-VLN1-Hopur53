from logic.MainLogic import MainLogic
from models.Employee import Employee

from ui.PrinterUI import PrinterUI
from ui.InputUI import InputUI

class EmployeeUI:

    def __init__(self, employee_id):
        self.items_per_page = 10

        self.logic = MainLogic()
        self.printer = PrinterUI()
        self.input = InputUI()

        self.employee_id = employee_id
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
                if self.create_employee():
                    self.success_msg = "New employee has been created"
                    self.view(True)
            elif action == '2':
                self.view()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    # Prints out all employee
    def view(self, created = False):
        current_page = 1
        while True:   
            employees = self.logic.get_all_employees()
            employees_count = len(employees)
            last_page = int(employees_count / self.items_per_page) + (employees_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else employees_count

            self.printer.header("View employees")
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
            print("ID:\t\t\t\t{}\nRole:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\nLocation:\t\t\t{}\n".format(employee_id, employee.role, employee.name, employee.email, employee.ssn, employee.phone, employee.homephone, employee.address, employee.postal, employee.location))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(employee_id)
            elif action == 'd' or action == 'delete':
                if self.employee_id != employee_id:
                    if self.delete(employee_id):
                        self.success_msg = "Employee has been deleted"
                        break
                else:
                    self.warning_msg = "You can't delete yourself"
            else:
                self.warning_msg = "Please select available option"
            
    # Prints out single employee
    def create_employee(self):
        counter = 0
        role = ""
        name = ""
        email = ""
        ssn = ""
        phone = ""
        homephone = ""
        address = ""
        postal = ""
        location_id = ""

        warning_msg = ""
        location_id_page = 1
        role_page = 1
        while True:
            self.printer.header("Create employee")
            print("Role:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\nLocation ID:\t\t\t{}\n".format(role, name, email, ssn, phone, homephone, address, postal, location_id))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            next_input = True
            try:
                if counter == 0:
                    role_input = self.input.get_option("role", ["Admin", "Delivery", "Booking", "Mechanic", "Financial","Admin","Admin", "Delivery", "Booking", "Mechanic", "Financial","Admin","Admin", "Delivery", "Booking", "Mechanic", "Financial","Admin"], current_page=role_page, warning_msg=warning_msg)                       
                    warning_msg = ""

                    if role_input[0]:
                        role = role_input[1]
                    else:
                        next_input = False
                        warning_msg = role_input[1]
                        role_page = role_input[2]
                elif counter == 1:
                    name_input = self.input.get_input("name", ["required"], warning_msg=warning_msg)
                    if name_input[0]:
                        name = name_input[1]
                        warning_msg = ""
                    else:
                        next_input = False
                        warning_msg = name_input[1]
                elif counter == 2:
                    email_input = self.input.get_input("email", ["required", "email"], warning_msg=warning_msg)
                    if email_input[0]:
                        email = email_input[1]
                        warning_msg = ""
                    else:
                        next_input = False
                        warning_msg = email_input[1]
                elif counter == 3:
                    ssn_input = self.input.get_input("social security number", ["required", "ssn"], warning_msg=warning_msg)
                    if ssn_input[0]:
                        ssn = ssn_input[1]
                        warning_msg = ""
                    else:
                        next_input = False
                        warning_msg = ssn_input[1]
                elif counter == 4:
                    phone_input = self.input.get_input("mobile phone", ["required", "phone"], warning_msg=warning_msg)
                    if phone_input[0]:
                        phone = phone_input[1]
                        warning_msg = ""
                    else:
                        next_input = False
                        warning_msg = phone_input[1]
                elif counter == 5:
                    homephone_input = self.input.get_input("home phone", ["required", "phone"], warning_msg=warning_msg)
                    if homephone_input[0]:
                        homephone = homephone_input[1]
                        warning_msg = ""
                    else:
                        next_input = False
                        warning_msg = homephone_input[1]
                elif counter == 6:
                    address_input = self.input.get_input("address", ["required"], warning_msg=warning_msg)
                    if address_input[0]:
                        address = address_input[1]
                        warning_msg = ""
                    else:
                        next_input = False
                        warning_msg = address_input[1]
                elif counter == 7:
                    postal_input = self.input.get_input("postal code", ["required"], warning_msg=warning_msg)
                    if postal_input[0]:
                        postal = postal_input[1]
                        warning_msg = ""
                    else:
                        next_input = False
                        warning_msg = postal_input[1]
                elif counter == 8:
                    locations = self.logic.get_all_locations()
                    available_locations = [[location.id, "{}".format(location)] for location in locations]
                    location_input = self.input.get_option("location", available_locations, current_page=location_id_page, warning_msg=warning_msg)
                    warning_msg = ""
                    if location_input[0] == True:
                        location_id = location_input[1]
                    else:
                        next_input = False
                        warning_msg = location_input[1]
                        location_id_page = location_input[2]
                elif counter > 8:
                    new_employee = Employee(role, name, address, postal, ssn, phone, homephone, email, location_id)
                    confirmation = input("Are you sure you want to create this employee? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()

                    if confirmation == 'y':
                        self.logic.create_employee(new_employee)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break
    
    # Prints out table of employee
    def print_employees(self, employees, start, end, current_page, last_page):
        if len(employees) > 0:
            print("|{:^6}|{:^15}|{:^25}|{:^30}|{:^30}|{:^20}|{:^20}|{:^25}|{:^15}|{:^15}|".format("ID", "Role", "Name", "Email", "Social security number", "Mobile phone", "Home phone", "Address", "Postal code", "Location ID"))
            print('-' * 212)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<25}|{:<30}|{:<30}|{:<20}|{:<20}|{:<25}|{:<15}|{:<15}|".format(employees[i].id, employees[i].role, employees[i].name, employees[i].email, employees[i].ssn, employees[i].phone, employees[i].homephone, employees[i].address, employees[i].postal, employees[i].location_id))
            print("{:^212}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No employees found"

    # Create employee
    """def create(self):
        self.printer.header("Add employee")
        self.printer.new_line()
        self.printer.print_fail("Press q to go back")
        self.printer.new_line()
        try:
            role = self.input.get_option("role", ["admin", "delivery", "booking", "mechanic", "financial"])
            name = self.input.get_input("name")
            email = self.input.get_input("email", ["email"])
            ssn = self.input.get_input("social security number", ["ssn"])
            phone = self.input.get_input("mobile phone", ["phone"])
            homephone = self.input.get_input("home phone", ["phone"])
            address = self.input.get_input("address")
            postal = self.input.get_input("postal code")
            location = self.input.get_input("location")
            new_employee = Employee(role, name, address, postal, ssn, phone, homephone, email, location)
            self.logic.create_employee(new_employee)
            return True
        except ValueError:
            return False"""
       
    # Edit employee
    def edit(self, id):
        while True:
            updates = {}
            self.printer.header("Edit employee")
            self.printer.print_options(['Change role', 'Change email', 'Change mobile phone', 'Change home phone', 'Edit address', 'Edit postal code', 'Change location'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == 'q':
                break
            elif action == '1':
                try:
                    role = self.input.get_option("role", ["admin", "delivery", "booking", "mechanic", "financial"])
                    updates["role"] = role
                except ValueError:
                    break
            elif action == '2':
                try:
                    email = self.input.get_input("email", ["email"])
                    updates["email"] = email
                except ValueError:
                    break
            elif action == '3':
                try:
                    phone = self.input.get_input("mobile phone", ["phone"])
                    updates["phone"] = phone
                except ValueError:
                    break
            elif action == '4':
                try:
                    homephone = self.input.get_input("home phone", ["phone"])
                    updates["homephone"] = homephone
                except ValueError:
                    break
            elif action == '5':
                try:
                    address = self.input.get_input("address")
                    updates["address"] = address
                except ValueError:
                    break
            elif action == '6':
                try:
                    postal = self.input.get_input("postal")
                    updates["postal"] = postal
                except ValueError:
                    break
            elif action == '7':
                try:
                    location = self.input.get_input("location")
                    updates["location"] = location
                except ValueError:
                    break
            else:
                self.warning_msg = "Please select available option"

            if(len(updates) > 0):
                self.logic.update_employee(id, updates)
                self.success_msg = "{} has been modified".format(list(updates.keys())[0].capitalize())

    # Delete employee
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this employee? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_employee(id)
            return True
        return False

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
