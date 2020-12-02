from ui.EmployeeUI import EmployeeUI

from logic.MainLogic import MainLogic


class MainUI:
    def __init__(self, user_id = None):
        self.logic = MainLogic()

        self.employee = EmployeeUI()

        self.user_id = user_id

        self.display()

    def display(self):

        self.menu()

        while True:
            if self.user_id:
                print(self.user_id)    
            else:
                self.user_id = self.employee.login()
