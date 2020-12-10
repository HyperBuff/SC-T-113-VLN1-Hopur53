from repositories.Repository import Repository
from models.Customer import Customer


class CustomerRepository:

    def __init__(self):
        self.filename = 'data/customer.csv'
        self.fieldnames = ['name', 'address', 'postal', 'ssn', 'phone', 'email', 'country', 'id']

    def create(self, customer: Customer):
        row = dict((key, getattr(customer, key)) for key in self.fieldnames)
        Repository().create(self.filename, self.fieldnames, row)
        return customer

    def read(self):
        rows = Repository().read(self.filename)
        customers = [Customer(row['name'], row['address'], row['postal'], row['ssn'], row['phone'], row['email'], row['country'], row['id']) for row in rows]
        return customers
    
    def update(self, id, updates: dict):
        return Repository().update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository().delete(self.filename, self.fieldnames, id)