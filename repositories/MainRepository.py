
from repositories.EmployeeRepository import EmployeeRepository
from models.Employee import Employee

from repositories.ContractRepository import ContractRepository
from models.Contract import Contract

from repositories.LocationRepository import LocationRepository
from models.Location import Location

from repositories.VehicleRepository import VehicleRepository
from models.Vehicle import Vehicle

from repositories.VehicleTypeRepository import VehicleTypeRepository
from models.VehicleType import VehicleType

from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer

class MainRepository:
    def __init__(self):
        self.employee = EmployeeRepository()
        self.contract = ContractRepository()
        self.location = LocationRepository()
        self.vehicle = VehicleRepository()
        self.vehicletype = VehicleTypeRepository()
        self.customer = CustomerRepository()

    # Basic CRUD for employees 
    def get_all_employees(self):
        return self.employee.read()

    def create_employee(self, employee):
        return self.employee.create(employee)

    def update_employee(self, id, updates):
        return self.employee.update(id, updates)

    def delete_employee(self, id):
        return self.employee.delete(id)

    # Basic CRUD for contracts
    def get_all_contracts(self):
        return self.contract.read()

    def create_contract(self, contract):
        return self.contract.create(contract)

    def update_contract(self, id, updates):
        return self.contract.update(id, updates)

    def delete_contract(self, id):
        return self.contract.delete(id)

    # Basic CRUD for destinations
    def get_all_locations(self):
        return self.location.read()

    def create_location(self, destination):
        return self.location.create(destination)

    def update_location(self, id, updates):
        return self.location.update(id, updates)

    def delete_location(self, id):
        return self.location.delete(id)

    #  Basic CRUD for vehicles
    def get_all_vehicles(self):
        return self.vehicle.read()

    def create_vehicle(self, vehicle):
        return self.vehicle.create(vehicle)

    def update_vehicle(self, id, updates):
        return self.vehicle.update(id, updates)

    def delete_vehicle(self, id):
        return self.vehicle.delete(id)

    # Basic CRUD for vehicle types
    def get_all_vehicletypes(self):
        return self.vehicletype.read()

    def create_vehicletype(self, vehicletype):
        return self.vehicletype.create(vehicletype)

    def update_vehicletype(self, id, updates):
        return self.vehicletype.update(id, updates)

    def delete_vehicletype(self, id):
        return self.vehicletype.delete(id)
    
    # Basic CRUD for customers
    def get_all_customers(self):
        return self.customer.read()

    def create_customer(self, customer):
        return self.customer.create(customer)

    def update_customer(self, id, updates):
        return self.customer.update(id, updates)

    def delete_customer(self, id):
        return self.customer.delete(id)