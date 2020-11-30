
from repositories.EmployeeRepository import EmployeeRepository

from models.Employee import Employee

class MainRepository:
    
    def get_all_employee(self):
        return EmployeeRepository().read()

