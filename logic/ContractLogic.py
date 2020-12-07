from repositories.MainRepository import MainRepository

class ContractLogic:

    def __init__(self):
        self.rep = MainRepository()
    
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