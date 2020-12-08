#Employee Logic
from logic.EmployeeLogic import EmployeeLogic
#Contract Logic
from logic.ContractLogic import ContractLogic
#Vehicle Logic
from logic.VehicleLogic import VehicleLogic
#Vehicle Logic
from logic.VehicleTypeLogic import VehicleTypeLogic
#Location Logic
from logic.LocationLogic import LocationLogic

class MainLogic:
    def __init__(self):
        self.employee = EmployeeLogic()
        self.contract = ContractLogic()
        self.vehicle = VehicleLogic()
        self.vehicletype = VehicleTypeLogic()
        self.location = LocationLogic()

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

    #Vehicle type Logic
    def get_all_vehicletypes(self):
        return self.vehicletype.get_all_vehicletypes()

    def get_vehicletype_by_id(self, vehicle_id):
        return self.vehicletype.get_vehicletype_by_id(vehicle_id)

    def create_vehicletype(self, vehicle):
        return self.vehicletype.create(vehicle)

    def update_vehicletype(self, id, updates):
        return self.vehicletype.update(id, updates)

    def delete_vehicletype(self, id):
        return self.vehicletype.delete(id)

    #Location Logic
    def get_all_locations(self):
        return self.location.get_all_locations()

    def get_location_by_id(self, location_id):
        return self.location.get_location_by_id(location_id)

    def create_location(self, vehicle):
        return self.location.create(vehicle)

    def update_location(self, id, updates):
        return self.location.update(id, updates)

    def delete_location(self, id):
        return self.location.delete(id)
