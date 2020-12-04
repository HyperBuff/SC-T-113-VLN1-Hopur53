from repositories.MainRepository import MainRepository

class Contract_Logic:

    def __init__(self):
        self.rep = MainRepository()
    
    def create(self, employee):
        self.rep.create_employee(employee)

    def get_all_contracts(self):
        return self.rep.get_all_employees()

    def update(self, id, updates):
        return self.rep.update_contract(id, updates)

    def delete(self, id):
        return self.rep.delete_contract(id)
    
    def get_contract_by_id(self, contract_id):
        contracts = self.get_all_contracts()

        for contract in contracts:
            if contract.id == contract_id:
                return contract
        return None

    def amount_due():
        pass