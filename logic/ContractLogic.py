from repositories.MainRepository import MainRepository
from logic.EmployeeLogic import EmployeeLogic
from logic.VehicleLogic import VehicleLogic
from logic.VehicleTypeLogic import VehicleTypeLogic

from datetime import datetime

class ContractLogic:

    def __init__(self):
        self.rep = MainRepository()
        self.employee = EmployeeLogic()
        self.vehicle = VehicleLogic()
        self.vehicletype = VehicleTypeLogic()

        self.date_format = "%d/%m/%Y"
    
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
                if key == "status": # {"status": "open"}
                    if contract.contract_status.lower() != filters[key]:
                        valid_contract = False
                if key == "pickup": # {"pickup": True}
                    if filters[key]:
                        if contract.pickup_date == "":
                            valid_contract = False
                    else:
                        if contract.pickup_date != "":
                            valid_contract = False
                if key == "dropoff": # {"pickup": True}
                    if filters[key]:
                        if contract.dropoff_date == "":
                            valid_contract = False
                    else:
                        if contract.dropoff_date != "":
                            valid_contract = False
                if key == "date": # {"date": ["15/12/2020", "22/12/2020"]}
                    date_from = datetime.strptime(contract.date_from, self.date_format)
                    date_to = datetime.strptime(contract.date_to, self.date_format)
                    check_date_from = datetime.strptime(filters[key][0], self.date_format)
                    check_date_to = datetime.strptime(filters[key][1], self.date_format)

                    if date_from < check_date_from or date_to > check_date_to:
                        valid_contract = False
            if valid_contract:
                results.append(contract)
        return results


    def contract_set_pickup(self, contract_id, date):

        updates = {"pickup_date": date}
        contract = self.get_contract_by_id(contract_id)

        days_to_early = (datetime.strptime(contract.date_from, self.date_format) - datetime.strptime(date, self.date_format)).days

        if days_to_early > 0:
            try:
                new_total = str(round(int(contract.total) + 1.20 * int(self.vehicletype.get_vehicletype_by_id(self.vehicle.get_vehicle_by_id(contract.vehicle_id)))))
                updates["total"] = new_total
            except ValueError:
                pass

        self.update(contract_id, updates)

    def contract_set_dropoff(self, contract_id, date):

        updates = {"dropoff_date": date}
        contract = self.get_contract_by_id(contract_id)

        days_to_late = (datetime.strptime(date, self.date_format) - datetime.strptime(contract.date_from, self.date_format)).days

        if days_to_late > 0:
            try:
                new_total = str(round(int(contract.total) + 1.20 * int(self.vehicletype.get_vehicletype_by_id(self.vehicle.get_vehicle_by_id(contract.vehicle_id)))))
                updates["total"] = new_total
                if int(contract.paid) >= int(new_total):
                    updates["contract_status"] = "Closed"
            except ValueError:
                pass
        else:
            try:
                if int(contract.paid) >= int(contract.total):
                    updates["contract_status"] = "Closed"
            except ValueError:
                pass

        self.update(contract_id, updates)

    def pay_to_contract(self, contract_id, amount):
        contract = self.get_contract_by_id(contract_id)
        updates = {}

        try:
            new_amount = int(contract.paid) + int(amount)
            updates["paid"] = str(new_amount)
            if new_amount >= int(contract.total) and contract.dropoff_date != "":
                updates["contract_status"] = "Closed"
        except ValueError:
            pass
        self.update(contract_id, updates)

