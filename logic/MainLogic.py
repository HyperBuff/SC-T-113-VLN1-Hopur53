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
#Customer Logic
from logic.CustomerLogic import CustomerLogic

class MainLogic:
    def __init__(self):
        self.employee = EmployeeLogic()
        self.contract = ContractLogic()
        self.vehicle = VehicleLogic()
        self.vehicletype = VehicleTypeLogic()
        self.location = LocationLogic()
        self.customer = CustomerLogic()

    #Emplyee Logic
    def login(self, email):
        return self.employee.get_user_id_from_email(email)
    
    def get_all_employees(self):
        return self.employee.get_all_employees()

    def get_employee_by_id(self, id):
        return self.employee.get_employee_by_id(id)

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

    def get_contract_by_id(self, id):
        return self.contract.get_contract_by_id(id)

    def create_contract(self, contract):
        return self.contract.create(contract)

    def update_contract(self, id, updates):
        return self.contract.update(id, updates)

    def delete_contract(self, id):
        return self.contract.delete(id)

    def filter_contracts(self, filters):
        return self.contract.filter_contracts(filters)

    def contract_set_pickup(self, contract_id, date):
        return self.contract.contract_set_pickup(contract_id, date)

    def contract_set_dropoff(self, contract_id, date):
        return self.contract.contract_set_dropoff(contract_id, date)

    def pay_to_contract(self, contract_id, amount):
        return self.contract.pay_to_contract(contract_id, amount)

    #Vehicle Logic
    def get_all_vehicles(self):
        return self.vehicle.get_all_vehicles()

    def get_vehicle_by_id(self, id):
        return self.vehicle.get_vehicle_by_id(id)

    def create_vehicle(self, vehicle):
        return self.vehicle.create(vehicle)

    def update_vehicle(self, id, updates):
        return self.vehicle.update(id, updates)

    def delete_vehicle(self, id):
        return self.vehicle.delete(id)

    def get_all_available_vehicles(self):
        return self.vehicle.get_all_available_vehicles()

    def filter_vehicles(self, filters):
        return self.vehicle.filter_vehicles(filters)

    #Vehicle type Logic
    def get_all_vehicletypes(self):
        return self.vehicletype.get_all_vehicletypes()

    def get_vehicletype_by_id(self, id):
        return self.vehicletype.get_vehicletype_by_id(id)

    def create_vehicletype(self, vehicletype):
        return self.vehicletype.create(vehicletype)

    def update_vehicletype(self, id, updates):
        return self.vehicletype.update(id, updates)

    def delete_vehicletype(self, id):
        return self.vehicletype.delete(id)

    #Location Logic
    def get_all_locations(self):
        return self.location.get_all_locations()

    def get_location_by_id(self, id):
        return self.location.get_location_by_id(id)

    def create_location(self, location):
        return self.location.create(location)

    def update_location(self, id, updates):
        return self.location.update(id, updates)

    def delete_location(self, id):
        return self.location.delete(id)

    #Customer Logic
    def get_all_customers(self):
        return self.customer.get_all_customers()

    def get_customer_by_id(self, id):
        return self.customer.get_customer_by_id(id)

    def create_customer(self, customer):
        return self.customer.create(customer)

    def update_customer(self, id, updates):
        return self.customer.update(id, updates)

    def delete_customer(self, id):
        return self.customer.delete(id)

