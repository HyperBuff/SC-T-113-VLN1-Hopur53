#Employee Logic
from logic.EmployeeLogic import EmployeeLogic
#Contract Logic
from logic.ContractLogic import ContractLogic
#Vehicle Logic
from logic.VehicleLogic import VehicleLogic

class MainLogic:
    def __init__(self):
        self.employee = EmployeeLogic()
        self.contract = ContractLogic()
        self.vehicle = VehicleLogic()

    #Emplyee Logic
    def login(self, email):
        return self.employee.get_user_id_from_email(email)
    
    def get_all_employees(self):
        return self.employee.get_all_employees()

    def get_employee_by_id(self, user_id):
        return self.employee.get_employee_by_id(user_id)

    def create_employee(self, employee):
        return self.employee.create(employee)

    def update_employee(self, id, updates):
        return self.employee.update(id, updates)

    def delete_employee(self, id):
        return self.employee.delete(id)

    def is_email_valid(self, email):
        return self.employee.is_email_valid(email)

    def is_ssn_valid(self, ssn):
        return self.employee.is_ssn_valid(ssn)

    def is_phone_number_valid(self, phone):
        return self.employee.is_phone_number_valid(phone)

    #Contract Logic
    def get_all_contracts(self):
        return self.contract.get_all_contracts()

    def get_contract_by_id(self, contract_id):
        return self.contract.get_contract_by_id(contract_id)

    def create_contract(self, contract):
        return self.contract.create(contract)

    def update_contract(self, id, updates):
        return self.contract.update(id, updates)

    def delete_contract(self, id):
        return self.contract.delete(id)

    #Vehicle Logic
    def get_all_vehicles(self):
        return self.vehicle.get_all_vehicles()

    def get_vehicle_by_id(self, vehicle_id):
        return self.vehicle.get_vehicle_by_id(vehicle_id)

    def create_vehicle(self, vehicle):
        return self.vehicle.create(vehicle)

    def update_vehicle(self, id, updates):
        return self.vehicle.update(id, updates)

    def delete_vehicle(self, id):
        return self.vehicle.delete(id)
