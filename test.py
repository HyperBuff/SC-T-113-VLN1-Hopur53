from repositories.EmployeeRepository import EmployeeRepository
from models.Employee import Employee

r = EmployeeRepository()

em = Employee('admin', 'Sigg', 'dd', '400', '8554331122', '9704432', '2331122', 'raggi@gm.com')

r.create(em)
