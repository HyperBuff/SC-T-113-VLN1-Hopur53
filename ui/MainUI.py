from ui.EmployeeUI import EmployeeUI
from ui.VehicleUI import VehicleUI

from logic.MainLogic import MainLogic


class MainUI:
    def __init__(self, user_id = None):
        self.logic = MainLogic()


        self.user_id = user_id
        self.name = None
        self.role = None
        

        self.display()

    def display(self):
        action = ""
        while not action == 'q':

            if self.user_id:
                user = self.logic.employee.get_employee_by_id(self.user_id)

                self.name = user.name
                self.role = user.role.lower()

                self.menu()
            else:
                self.header("NaN Air - Rentals")

                print("\n\33[;31mPress q to quit the program\33[;0m\n")
                action = input("\nEnter email to login: ").lower()

                if not action == 'q':

                    self.user_id = self.logic.login(action)


    def menu(self):

        
        self.header("NaN Air - Rentals")
        print(f"{self.name}")
        print(f"{self.role}")

        if self.role == "admin":
            self.admin()


        '''
        elif self.role == "delivery":
            self.delivery()
        elif self.role == "booking":
            self.booking()
        '''

    def admin(self):
        print("\n1. Contracts\n2. Vehicles\n3. Employees\n4. Locations\n5. Financials\n\n\33[;31mPress q to logout\33[;0m\n")
        action = input("\nChoose an option: ").lower()
        
        if action == str(1):
            self.contracts()
        elif action == str(2):
            self.vehicles()
        elif action == str(3):
            self.employees()
        elif action == str(4):
            self.locations()
        elif action == str(5):
            self.financials()
        elif action == 'q':
            self.logout()
        


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
        self.user_id = None
        self.name = None
        self.role = None

    def header(self, title):
        print("-" * 50)
        print("|{:^48}|".format(title))
        print("-" * 50)
        print()



