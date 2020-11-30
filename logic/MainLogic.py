from logic.EmployeeLogic import EmployeeLogic

class MainLogic:
    def get_em(self):
        return EmployeeLogic().get_list_of_employee()