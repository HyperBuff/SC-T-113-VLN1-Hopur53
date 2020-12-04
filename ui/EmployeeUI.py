import math



from logic.MainLogic import MainLogic
from models.Employee import Employee

from ui.PrinterUI import PrinterUI

class EmployeeUI:

    def __init__(self):
        self.items_per_page = 10
        self.logic = MainLogic()

        self.printer = PrinterUI()


    # Employee Menu

    def menu(self):

        warning_msg = ""

        while True:
            self.printer.header("Employees Menu")
            self.printer.print_options(['Create an employee', 'View employees'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_warning(warning_msg)

            action = input("Choose an option: ").lower()

            if action == '1':
                if self.create():
                    self.view(success_msg = "New employee has been created")
            elif action == '2':
                self.view()
            elif action == 'q':
                break
            else:
                warning_msg = "Please select available option"

    # View Employees

    def view(self, current_page = 1, warning_msg = "", success_msg = ""):

        while True:   
            self.printer.header("View employees")

            employees = self.logic.get_all_employees()
            employees_count = len(employees)


            last_page = math.ceil(employees_count / self.items_per_page)

            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else employees_count


            self.print_employees(employees, start, end, current_page, last_page)

            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            if not success_msg == "":
                self.printer.print_success(success_msg)
            else:
                self.printer.print_warning(warning_msg)

            action = input("(N)ext page / (P)revious page / (S)elect employee: ").lower()

            if action == 'q':
                break
            elif action == 'n':
                if current_page >= last_page:
                    current_page = last_page
                    warning_msg = "You are currenly on the last page"
                else:
                    current_page += 1
            elif action == 'p':
                if current_page > 1:
                    current_page -= 1
                else:
                    current_page = 1
                    warning_msg = "You are currenly on the first page"
            elif action == 's':
                employee_id = input("Select employee by ID: ")
                employee = self.logic.get_employee_by_id(employee_id)
                if employee is None:
                    warning_msg = "Employee not found"
                else:
                    success_msg = self.select_employee(employee_id)



    def select_employee(self, employee_id):
        
        warning_msg = ""
        success_msg = ""

        while True:

            employee = self.logic.get_employee_by_id(employee_id)

            self.printer.header("View employee")

            print("ID:\t\t\t\t{}\nRole:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\n".format(employee_id, employee.role, employee.name, employee.email, employee.ssn, employee.phone, employee.homephone, employee.address, employee.postal))

            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            if not warning_msg == "":
                self.printer.print_warning(warning_msg)
            else:
                self.printer.print_success(success_msg)

            action = input("(E)dit / (D)elete: ").lower()

            if action == 'q':
                break
            elif action == 'e':
                success_msg = self.edit(employee_id)
            elif action == 'd':
                if self.delete(employee_id):
                    return "Employee has been deleted"
        return ""
        
            
    def print_employees(self, employees, start, end, current_page, last_page):
        print("|{:^6}|{:^15}|{:^30}|{:^40}|{:^30}|{:^20}|{:^20}|{:^30}|{:^15}|".format("ID", "Role", "Name", "Email", "Social security number", "Mobile phone", "Home phone", "Address", "Postal code"))
        print('-' * 216)
        for i in range(start, end):
            print("|{:^6}|{:<15}|{:<30}|{:<40}|{:<30}|{:<20}|{:<20}|{:<30}|{:<15}|".format(employees[i].id, employees[i].role, employees[i].name, employees[i].email, employees[i].ssn, employees[i].phone, employees[i].homephone, employees[i].address, employees[i].postal))
        print("{:^216}".format("Page {} of {}".format(current_page, last_page)))
        self.printer.new_line()

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
            elif not self.is_email_valid(email):
                self.printer.print_warning("Email is not valid")
            else:
                break

        while True:
            ssn = input("\tEnter social security number: ")
            if ssn == 'q':
                return
            elif len(ssn) < 1:
                self.printer.print_warning("Social security number must been at least 1 character")
            elif not self.is_ssn_valid(ssn):
                self.printer.print_warning("Social security number is not valid, please try again")
            else:
                break

        while True:
            phone = input("\tEnter mobile phone: ")
            if phone == 'q':
                return
            if len(phone) < 1:
                self.printer.print_warning("Mobile phone must been at least 1 character")
            else:
                break

        while True:
            homephone = input("\tEnter home phone: ")
            if homephone == 'q':
                return
            if len(homephone) < 1:
                self.printer.print_warning("Home phone must been at least 1 character")
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


  
    def edit(self, id):

        while True:

            updates = {}
            self.printer.header("Edit employee")
            self.printer.print_options(['Change role', 'Change email', 'Change mobile phone', 'Change home phone', 'Edit address', 'Edit postal code'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()

            action = input("Choose an option: ").lower()

            if action == 'q':
                break
            elif action != '1':
                new_value = input("Change to: ")
            
            if new_value == 'q':
                break
            
            if len(new_value) < 1:
                print("")
                break

            if action == '1':
                updates["role"] = self.select_role()
            elif action == '2':
                updates["email"] = new_value
            elif action == '3':
                updates["phone"] = new_value
            elif action == '4':
                updates["homephone"] = new_value
            elif action == '5':
                updates["address"] = new_value
            elif action == '6':
                updates["postal"] = new_value

            self.logic.update_employee(id, updates)
        return "Employee has been modified successfully"

    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this employee? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_employee(id)
            return True
        return False

    
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

    def is_email_valid(self, email):
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

    def is_ssn_valid(self, ssn):
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
