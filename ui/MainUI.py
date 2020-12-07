from ui.EmployeeUI import EmployeeUI
from ui.VehicleUI import VehicleUI
from ui.LocationUI import LocationUI
from ui.ContractUI import ContractUI

from ui.PrinterUI import PrinterUI

from logic.MainLogic import MainLogic


class MainUI:
    def __init__(self, employee_id = None):
        self.logic = MainLogic()

        self.employee_id = employee_id
        self.name = None
        self.role = None

        self.printer = PrinterUI()
        
        self.success_msg = ""
        self.warning_msg = ""

        self.display()

    def display(self):
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
                self.print_msg()
                action = input("Enter email to login: ").lower()

                if not action == 'q':
                    login = self.logic.login(action)
                    if login is None:
                        self.warning_msg = "Account not found"
                    else:
                        self.employee_id = login
                else:
                    break


    def menu(self):
        if self.role.lower() == "admin":
            self.admin()
        else:
            self.logout()
            self.warning_msg = "No role assigned to user"

    def admin(self):
        while True:
            self.printer.header("NaN Air - Rentals")
            print(f"Logged in as: {self.name} ({self.role})")
            self.printer.new_line()
            self.printer.print_options(['Contracts', 'Vehicles', 'Employees', 'Locations', 'Financials'])
            self.printer.new_line(2)
            self.printer.print_fail('Press q to logout')
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == '1':
                self.contracts(self.employee_id)
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
                self.warning_msg = "Please select available option"

    def contracts(self, employee_id):
        contract = ContractUI(employee_id)
        contract.menu()

    def vehicles(self, employee_id):
        vehicle = VehicleUI()
        vehicle.menu()

    def employees(self):
        employee = EmployeeUI(self.employee_id)
        employee.menu()

    def locations(self):
        location = LocationUI()
        location.menu()
        pass

    def financials(self):
        pass

    def logout(self):
        self.employee_id = None
        self.name = None
        self.role = None

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