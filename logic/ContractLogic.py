from repositories.MainRepository import MainRepository
from logic.EmployeeLogic import EmployeeLogic

class ContractLogic:

    def __init__(self):
        self.rep = MainRepository()
        self.employee = EmployeeLogic()
    
    def create(self, contract):
        self.rep.create_contract(contract)

    def get_all_contracts(self):
        return self.rep.get_all_contracts()

    def update(self, id, updates):
        return self.rep.update_contract(id, updates)

    def delete(self, id):
        return self.rep.delete_contract(id)
    
    def get_contract_by_id(self, id):
        contracts = self.get_all_contracts()

        for contract in contracts:
            if contract.id == id:
                return contract
        return None

    def get_contract_from_location(self, employee_id):
        location_id = self.employee.get_employee_by_id(employee_id).location_id
        results = []
        contracts = self.get_all_contracts()
        for contract in contracts:
            if contract.location_id == location_id:
                results.append(contract)
        return results