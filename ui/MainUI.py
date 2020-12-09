from ui.EmployeeUI import EmployeeUI
from ui.VehicleUI import VehicleUI
from ui.LocationUI import LocationUI
from ui.ContractUI import ContractUI
from ui.FinanceUI import  FinanceUI

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
        if not self.role == "":
            while True:
                menu_options = self.menu_options()
                self.printer.header("NaN Air - Rentals")
                print(f"Logged in as: {self.name} ({self.role})")
                self.printer.new_line()
                self.printer.print_menu_options(menu_options)
                self.printer.new_line(2)
                self.printer.print_fail('Press q to logout')
                self.print_msg()
                action = input("Choose an option: ").lower()
                if action == 'q':
                    self.logout()
                    break
                try:
                    list(menu_options.values())[int(action)-1]()
                except:
                    self.warning_msg = "Please select available option"
        else:
            self.logout()
            self.warning_msg = "No role assigned to user"

    def menu_options(self):
        if self.role.lower() == "admin":
            return {
                "Contracts": self.contracts,
                "Vehicles": self.vehicles,
                "Employee": self.employees,
                "Locations": self.locations,
                "Financials": self.financials
            }
        elif self.role.lower() == "mechanic":
            return {
                "Vehicles": self.vehicles
            }
        elif self.role.lower() == "delivery":
            return {
                "Vehicles": self.vehicles,
                "Contracts": self.contracts
            }
        elif self.role.lower() == "booking":
            return {
                "Contracts": self.contracts,
                "Locations": self.locations
            }
        elif self.role.lower() == "financial":
            return {
                "Financials": self.financials
            }


    def contracts(self):
        ContractUI(self.employee_id, self.role)

    def vehicles(self):
        VehicleUI(self.employee_id, self.role)

    def employees(self):
        EmployeeUI(self.employee_id)

    def locations(self):
        LocationUI(self.employee_id, self.role)

    def financials(self):
        FinanceUI(self.employee_id, self.role)

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