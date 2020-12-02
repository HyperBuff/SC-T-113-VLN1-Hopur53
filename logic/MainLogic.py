from logic.EmployeeLogic import EmployeeLogic

class MainLogic:
    def __init__(self):
        self.employee = EmployeeLogic()

    
    def get_all(self):
        return self.employee.get_all_employees()

    def login(self, email):
        return self.employee.get_user_id_from_email(email)

    def get_employee_by_id(self, user_id):
        return self.employee.get_employee_by_id(user_id)