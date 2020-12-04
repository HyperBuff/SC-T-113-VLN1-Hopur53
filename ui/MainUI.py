from ui.EmployeeUI import EmployeeUI
from ui.VehicleUI import VehicleUI

from ui.PrinterUI import PrinterUI

from logic.MainLogic import MainLogic


class MainUI:
    def __init__(self, employee_id = None):
        self.logic = MainLogic()

        self.employee_id = employee_id
        self.name = None
        self.role = None

        self.printer = PrinterUI()        

        self.display()

    def display(self, warning_msg = ""):
        while True:
            if self.employee_id:
                user = self.logic.employee.get_employee_by_id(self.employee_id)

                self.name = user.name
                self.role = user.role

                self.menu()
            else:

                self.printer.header("NaN Air - Rentals")
                self.printer.new_line()
                self.printer.print_fail("Press q to quit")
                self.printer.print_warning(warning_msg)
                action = input("Enter email to login: ").lower()

                if not action == 'q':
                    login = self.logic.login(action)
                    if login is None:
                        warning_msg = "Account not found"
                    else:
                        self.employee_id = login
                else:
                    break


    def menu(self):
        self.printer.header("NaN Air - Rentals")

        print(f"Logged in as: {self.name} ({self.role})")

        if self.role.lower() == "admin":
            self.admin()
        else:
            self.printer.print_warning("No role assigned to user")
    

    def admin(self, warning_msg = ""):

        while True:
            self.printer.new_line()
            self.printer.print_options(['Contracts', 'Vehicles', 'Employees', 'Locations', 'Financials'])
            self.printer.new_line(2)
            self.printer.print_fail('Press q to logout')
            self.printer.print_warning(warning_msg)
            action = input("Choose an option: ").lower()
            
            if action == '1':
                self.contracts()
            elif action == '2':
                self.vehicles()
            elif action == '3':
                self.employees()
            elif action == '4':
                self.locations()
            elif action == '5':
                self.financials()
            elif action == 'q':
                self.logout()
                break
            else:
                warning_msg = "Please select available option"
        



    def contracts(self):
        pass

    def vehicles(self):
        vehicle = VehicleUI()
        vehicle.menu()

    def employees(self):
        employee = EmployeeUI()
        employee.menu()

    def locations(self):
        pass

    def financials(self):
        pass

    def logout(self):
        self.employee_id = None
        self.name = None
        self.role = None



