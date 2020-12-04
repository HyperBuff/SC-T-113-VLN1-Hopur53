
#Import Employees
from repositories.EmployeeRepository import EmployeeRepository
from models.Employee import Employee
#Import Contracts
from repositories.ContractRepository import ContractRepository
from models.Contract import Contract
#Import Destinations
from repositories.DestinationRepository import DestinationRepository
from models.Destination import Destination
#Import Vehicles
from repositories.VehicleRepository import VehicleRepository
from models.Vehicle import Vehicle
#Import VehicleTypes
from repositories.VehicleTypeRepository import VehicleTypeRepository
from models.VehicleType import VehicleType
#Import Customer
from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer

class MainRepository:
    #initalize
    def __init__(self):
        self.employee = EmployeeRepository()
        self.contract = ContractRepository()
        self.destination = DestinationRepository()
        self.vehicle = VehicleRepository()
        self.vehicletype = VehicleTypeRepository()
        self.customer = CustomerRepository()

    #Employees 
    def get_all_employees(self):
        return self.employee.read()

    def create_employee(self, employee):
        return self.employee.create(employee)

    def update_employee(self, id, updates):
        return self.employee.update(id, updates)

    def delete_employee(self, id):
        return self.employee.delete(id)

    #Contracts
    def get_all_contracts(self):
        return self.contract.read()

    def create_contract(self, contract):
        return self.contract.create(contract)

    def update_contract(self, id, updates):
        return self.contract.update(id, updates)

    def delete_contract(self, id):
        return self.contract.delete(id)

    #Destinations
    def get_all_destinations(self):
        return self.destination.read()

    def create_destination(self, destination):
        return self.destination.create(destination)

    def update_destination(self, id, updates):
        return self.destination.update(id, updates)

    def delete_destination(self, id):
        return self.destination.delete(id)

    #Vehicles
    def get_all_vehicles(self):
        return self.vehicle.read()

    def create_vehicle(self, vehicle):
        return self.vehicle.create(vehicle)

    def update_vehicle(self, id, updates):
        return self.vehicle.update(id, updates)

    def delete_vehicle(self, id):
        return self.vehicle.delete(id)

    #VehicleTypes
    def get_all_vehicletypes(self):
        return self.vehicletype.read()

    def create_vehicletype(self, vehicletype):
        return self.vehicletype.create(vehicletype)

    def update_vehicletype(self, id, updates):
        return self.vehicletype.update(id, updates)

    def delete_vehicletype(self, id):
        return self.vehicletype.delete(id)
    
    #Customers
    def get_all_customers(self):
        return self.customer.read()

    def create_customer(self, customer):
        return self.customer.create(customer)

    def update_customer(self, id, updates):
        return self.customer.update(id, updates)

    def delete_customer(self, id):
        return self.customer.delete(id)