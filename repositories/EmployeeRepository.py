from repositories.Repository import Repository
from models.Employee import Employee


class EmployeeRepository:

    def __init__(self):
        self.filename = 'data/employee.csv'
        self.fieldnames = ['role', 'name', 'address', 'postal', 'ssn', 'phone', 'homephone', 'email', 'id']

    def create(self, employee: Employee):
        row = dict((key, getattr(employee, key)) for key in self.fieldnames)
        Repository()._create(self.filename, self.fieldnames, row)
        return employee

    def read(self):
        rows = Repository()._read(self.filename)
        users = [Employee(row['role'], row['name'], row['address'], row['postal'], row['ssn'], row['phone'], row['homephone'], row['email'], row['id']) for row in rows]
        return users
    
    def update(self, id, updates: dict):
        return Repository()._update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository()._delete(self.filename, self.fieldnames, id)