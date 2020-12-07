
from repositories.Repository import Repository
from models.Contract import Contract


class ContractRepository:

    def __init__(self):
        self.filename = 'data/contract.csv'
        self.fieldnames = ['name', 'phone', 'email', 'address', 'vehicle_id', 'vehicle_status', 'employee_id', 'location_id', 'date_from', 'date_to', 'loan_date', 'loan_status', 'return_date', 'total', 'id']

    def create(self, contract: Contract):
        row = dict((key, getattr(contract, key)) for key in self.fieldnames)
        Repository()._create(self.filename, self.fieldnames, row)
        return contract

    def read(self):
        rows = Repository()._read(self.filename)
        contracts = [Contract(row['name'], row['phone'], row['email'], row['address'], row['vehicle_id'], row['vehicle_status'], row['employee_id'], row['location_id'], row['date_from'], row['date_to'], row['loan_date'], row['loan_status'], row['return_date'], row['total'], row['id']) for row in rows]
        return contracts
    
    def update(self, id, updates: dict):
        return Repository()._update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository()._delete(self.filename, self.fieldnames, id)