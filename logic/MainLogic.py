from logic.EmployeeLogic import EmployeeLogic

class MainLogic:
    def __init__(self):
        self.employee = EmployeeLogic()

    def login(self, email):
        return self.employee.get_user_id_from_email(email)
    
    def get_all_employees(self):
        return self.employee.get_all_employees()

    def get_employee_by_id(self, user_id):
        return self.employee.get_employee_by_id(user_id)

    def create_employee(self, employee):
        return self.employee.create(employee)