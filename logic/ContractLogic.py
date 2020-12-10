from repositories.MainRepository import MainRepository
from logic.EmployeeLogic import EmployeeLogic

from datetime import datetime

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

    def filter_contracts(self, filters):
        results = []
        contracts = self.get_all_contracts()
        for contract in contracts:
            valid_contract = True
            for key in filters.keys():
                if key == "vehicle": # {"vehicle": vehicle_id}
                    if contract.vehicle_id != filters[key]:
                        valid_contract = False
                if key == "location": # {"location": location_id}
                    if contract.location_id != filters[key]:
                        valid_contract = False
                if key == "employee": # {"employee": employee_id}
                    if contract.employee_id != filters[key]:
                        valid_contract = False
                if key == "status": # {"status": "available"}
                    if contract.contract_status.lower() != filters[key]:
                        valid_contract = False
                if key == "date": # {"date": ["15/12/2020", "22/12/2020"]}
                    date_format = "%d/%m/%Y"
                    date_from = datetime.strptime(contract.date_from, date_format)
                    date_to = datetime.strptime(contract.date_to, date_format)
                    check_date_from = datetime.strptime(filters[key][0], date_format)
                    check_date_to = datetime.strptime(filters[key][1], date_format)

                    if date_from < check_date_from or date_to > check_date_to:
                        valid_contract = False
            if valid_contract:
                results.append(contract)
        return results
