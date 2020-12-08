from logic.MainLogic import MainLogic
from models.Employee import Employee
from models.Location import Location

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

        self.menu()


    def create(self):
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
        
        location_id_page = 1
        role_page = 1
        while True:

            location = self.logic.get_location_by_id(location_id)
            if location is None:
                location = ""

            self.printer.header("Create employee")
            print(f"Role:\t\t\t\t{role}\nName:\t\t\t\t{name}\nEmail:\t\t\t\t{email}\nSocial security number:\t\t{ssn}\nMobile phone:\t\t\t{phone}\nHome phone:\t\t\t{homephone}\nAddress:\t\t\t{address}\nPostal code:\t\t\t{postal}\nLocation:\t\t\t{location}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.notification()
            next_input = True
            data = None
            try:
                if counter == 0:
                    data = self.input.get_option("role", ["Admin", "Delivery", "Booking", "Mechanic", "Financial"], current_page = role_page, warning_msg = self.warning_msg)
                    if data[0]:
                        role = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                        role_page = data[2]
                elif counter == 1:
                    data = self.input.get_input("name", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        name = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 2:
                    data = self.input.get_input("email", ["required", "email"], warning_msg = self.warning_msg)
                    if data[0]:
                        email = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 3:
                    data = self.input.get_input("social security number", ["required", "ssn"], warning_msg = self.warning_msg)
                    if data[0]:
                        ssn = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 4:
                    data = self.input.get_input("mobile phone", ["required", "phone"], warning_msg = self.warning_msg)
                    if data[0]:
                        phone = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 5:
                    data = self.input.get_input("home phone", ["required", "phone"], warning_msg = self.warning_msg)
                    if data[0]:
                        homephone = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 6:
                    data = self.input.get_input("address", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        address = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 7:
                    data = self.input.get_input("postal code", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        postal = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 8:
                    locations = self.logic.get_all_locations()
                    available_locations = [[location.id, location] for location in locations]
                    location_input = self.input.get_option("location", available_locations, current_page = location_id_page, warning_msg = self.warning_msg)
                    if location_input[0] == True:
                        location_id = location_input[1]
                    else:
                        next_input = False
                        self.warning_msg = location_input[1]
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

    # Prints out employee's menu
    def menu(self):
        while True:
            self.printer.header("Employees Menu")
            self.printer.print_options(['Create an employee', 'View employees'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                if self.create():
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
            self.print(employees, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()

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
                employee_id = input("Select employee by ID: ").lower()
                if employee_id == 'q':
                    break
                employee = self.logic.get_employee_by_id(employee_id)
                if employee is None:
                    self.warning_msg = "Employee not found"
                else:
                    self.employee(employee_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single employee
    def employee(self, employee_id):
        while True:
            employee = self.logic.get_employee_by_id(employee_id)
            self.printer.header("View employee")
            print("ID:\t\t\t\t{}\nRole:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\nLocation:\t\t\t{}\n".format(employee_id, employee.role, employee.name, employee.email, employee.ssn, employee.phone, employee.homephone, employee.address, employee.postal, self.logic.get_location_by_id(employee.location_id)))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
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
    
    # Prints out table of employee
    def print(self, employees, start, end, current_page, last_page):
        if len(employees) > 0:
            print("|{:^6}|{:^15}|{:^25}|{:^30}|{:^30}|{:^20}|{:^20}|{:^25}|{:^15}|{:^15}|".format("ID", "Role", "Name", "Email", "Social security number", "Mobile phone", "Home phone", "Address", "Postal code", "Location"))
            print('-' * 212)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<25}|{:<30}|{:<30}|{:<20}|{:<20}|{:<25}|{:<15}|{:<15}|".format(employees[i].id, employees[i].role, employees[i].name, employees[i].email, employees[i].ssn, employees[i].phone, employees[i].homephone, employees[i].address, employees[i].postal, self.logic.get_location_by_id(employees[i].location_id).__str__()))
            print("{:^212}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No employees found"
  

    def edit(self, employee_id):
        location_id_page = 1
        role_page = 1
        while True:
            employee = self.logic.get_employee_by_id(employee_id)
            update = {}
            self.printer.header("Edit employee")
            print(f"ID:\t\t\t\t{employee_id}\nRole:\t\t\t\t{employee.role}\nName:\t\t\t\t{employee.name}\nEmail:\t\t\t\t{employee.email}\nSocial security number:\t\t{employee.ssn}\nMobile phone:\t\t\t{employee.phone}\nHome phone:\t\t\t{employee.homephone}\nAddress:\t\t\t{employee.address}\nPostal code:\t\t\t{employee.postal}\nLocation:\t\t\t{self.logic.get_location_by_id(employee.location_id)}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit role', 'Edit email', 'Edit mobile phone', 'Edit home phone', 'Edit address', 'Edit postal code', 'Edit location'])
            self.printer.new_line()
            self.notification()
            while True:
                action = input("Choose an option: ").lower()
                data = None
                try:
                    if action == "q":
                        return
                    elif action == "1":
                        while True:
                            data = self.input.get_option("role", ["Admin", "Delivery", "Booking", "Mechanic", "Financial"], current_page = role_page, warning_msg = self.warning_msg)
                            if data[0]:
                                update["role"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                role_page = data[2]
                                
                    elif action == "2":
                        while True:
                            data = self.input.get_input("email", ["required", "email"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["email"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "3":
                        while True:
                            data = self.input.get_input("mobile phone", ["required", "phone"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["phone"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "4":
                        while True:
                            data = self.input.get_input("home phone", ["required", "phone"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["homephone"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "5":
                        while True:
                            data = self.input.get_input("address", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["address"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "6":
                        while True:
                            data = self.input.get_input("postal code", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["postal"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "7":
                        while True:
                            locations = self.logic.get_all_locations()
                            available_locations = [[location.id, location] for location in locations]
                            data = self.input.get_option("location", available_locations, current_page = location_id_page, warning_msg = self.warning_msg)
                            if data[0] == True:
                                update["location_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                location_id_page = data[2]
                    if(len(update) > 0):
                        self.logic.update_employee(employee_id, update)
                        self.success_msg = "Employee has been modified"
                    break
                except ValueError:
                    break

    # Delete employee
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this employee? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_employee(id)
            return True
        return False

    # Outputs warnings and success messages
    def notification(self):
        if not self.warning_msg == "":
            self.printer.print_warning(self.warning_msg)
            self.warning_msg = ""
        elif not self.success_msg == "":
            self.printer.print_success(self.success_msg)
            self.success_msg = ""
        else:
            self.printer.new_line()