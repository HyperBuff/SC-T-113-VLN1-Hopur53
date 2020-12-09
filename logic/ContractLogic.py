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

    def get_contract_from_location(self, location_id):
        results = []
        contracts = self.get_all_contracts()
        for contract in contracts:
            if contract.location_id == location_id:
                results.append(contract)
        return results

    def get_contracts_from_vehicle(self, vehicle_id):
        results = []
        contracts = self.get_all_contracts()
        for contract in contracts:
            if contract.vehicle_id == vehicle_id:
                results.append(contract)
        return results

    def get_closed_contracts(self):
        results = []
        contracts = self.get_all_contracts()
        for contract in contracts:
            if contract.status.lower() == "closed":
                results.append(contract)
        return results
    
    def get_open_contracts(self):
        results = []
        contracts = self.get_all_contracts()
        for contract in contracts:
            if contract.status.lower() == "open":
                results.append(contract)
        return results