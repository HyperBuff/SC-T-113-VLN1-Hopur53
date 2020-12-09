
from repositories.Repository import Repository
from models.Contract import Contract


class ContractRepository:

    def __init__(self):
        self.filename = 'data/contract.csv'
        self.fieldnames = ['customer_id', 'vehicle_id', 'vehicle_status', 'employee_id', 'location_id', 'date_from', 'date_to', 'contract_date', 'contract_status', 'pickup_date', 'dropoff_date', 'total', 'id']

    def create(self, contract: Contract):
        row = dict((key, getattr(contract, key)) for key in self.fieldnames)
        Repository()._create(self.filename, self.fieldnames, row)
        return contract

    def read(self):
        rows = Repository()._read(self.filename)
        contracts = [Contract(row['customer_id'], row['vehicle_id'], row['vehicle_status'], row['employee_id'], row['location_id'], row['date_from'], row['date_to'], row['contract_date'], row['contract_status'], row['pickup_date'], row['dropoff_date'], row['total'], row['id']) for row in rows]
        return contracts
    
    def update(self, id, updates: dict):
        return Repository()._update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository()._delete(self.filename, self.fieldnames, id)