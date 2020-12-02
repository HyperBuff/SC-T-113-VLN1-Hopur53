
from repositories.EmployeeRepository import EmployeeRepository

from models.Employee import Employee

class MainRepository:

    def __init__(self):
        self.employee = EmployeeRepository()
    
    def get_all_employees(self):
        return self.employee.read()

    def create_employee(self, employee):
        return self.employee.create(employee)