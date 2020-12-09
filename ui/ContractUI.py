#Datetime
from datetime import datetime
#Logic
from logic.MainLogic import MainLogic
#Models
from models.Contract import Contract
from models.Customer import Customer
from models.Vehicle import Vehicle
from models.Employee import Employee
from models.Location import Location
#UI Functions
from ui.PrinterUI import PrinterUI
from ui.InputUI import InputUI



class ContractUI:

    def __init__(self, employee_id):
        
        self.items_per_page = 10

        self.logic = MainLogic()

        self.printer = PrinterUI()
        self.input = InputUI()

        self.employee_id = employee_id

        self.success_msg = ""
        self.warning_msg = ""

        self.menu()


    def create(self):
        counter = 0

        customer_id = ""
        vehicle_id = ""
        
        employee_id = self.employee_id
        location_id = ""
        date_from = ""
        date_to = ""

        contract_date = self.input.get_date()
        contract_status = "Open"
        pickup_date = ""
        dropoff_date = ""

        total = ""
        
        customer_id_page = 1
        vehicle_id_page = 1
        while True:

            customer = self.logic.get_customer_by_id(customer_id)
            vehicle = self.logic.get_vehicle_by_id(vehicle_id)

            if customer is None:
                customer = ""
            if vehicle is None:
                vehicle = ""

            self.printer.header("Create contract")
            print(f"Customer:\t\t\t\t{customer}\nVehicle:\t\t\t\t{vehicle}\nDate from:\t\t\t\t{date_from}\nDate to:\t\t\t\t{date_to}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.notification()
            next_input = True
            data = None
            try:
                if counter == 0:
                    customers = self.logic.get_all_customers()
                    available_customers = [[customer.id, customer] for customer in customers]
                    customer_input = self.input.get_option("customer", available_customers, current_page = customer_id_page, warning_msg = self.warning_msg)
                    if customer_input[0] == True:
                        customer_id = customer_input[1]
                    else:
                        next_input = False
                        self.warning_msg = customer_input[1]
                        customer_id_page = customer_input[2]
                elif counter == 1:
                    vehicles = self.logic.get_all_vehicles()
                    available_vehicles = [[vehicle.id, vehicle] for vehicle in vehicles]
                    vehicle_input = self.input.get_option("vehicle", available_vehicles, current_page = vehicle_id_page, warning_msg = self.warning_msg)
                    if vehicle_input[0] == True:
                        vehicle_id = vehicle_input[1]
                    else:
                        next_input = False
                        self.warning_msg = vehicle_input[1]
                        vehicle_id_page = vehicle_input[2]
                elif counter == 2:
                    data = self.input.get_input("date from", ["required", "date"], warning_msg = self.warning_msg)
                    if data[0]:
                        date_from = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 3:
                    data = self.input.get_input("date to", ["required", "date"], warning_msg = self.warning_msg)
                    if data[0]:
                        date_to = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter > 3:

                    self.logic.update_vehicle(vehicle_id, {"status": "Unavailable"})
                    vehicle_status = self.logic.get_vehicle_by_id(vehicle_id).status
                    vehicle = self.logic.get_vehicle_by_id(vehicle_id)
                    location_id = vehicle.location_id

                    date_format = "%d/%m/%Y"

                    days = datetime.strptime(date_to, date_format) - datetime.strptime(date_from, date_format)
                    total = int(days.days) * int(self.logic.get_vehicletype_by_id(vehicle.vehicle_type_id).rate)

                    new_contract = Contract(customer_id,vehicle_id,vehicle_status,employee_id,location_id,date_from,date_to,contract_date,contract_status,pickup_date,dropoff_date,total)
                    confirmation = input("Are you sure you want to create this contract? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_contract(new_contract)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break

    # Prints out contract's menu
    def menu(self):
        while True:
            self.printer.header("Contracts Menu")
            self.printer.print_options(['Create an contract', 'View contracts'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                if self.create():
                    self.success_msg = "New contract has been created"
                    self.view(True)
            elif action == '2':
                self.view()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    # Prints out all contract
    def view(self, created = False):
        current_page = 1
        while True:   
            contracts = self.logic.get_all_contracts()
            contracts_count = len(contracts)
            last_page = int(contracts_count / self.items_per_page) + (contracts_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else contracts_count

            self.printer.header("View contracts")
            self.print(contracts, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("(N)ext page / (P)revious page / (S)elect contract: ").lower()

            if action == 'q':
                break
            elif action == 'n' or action == "next":
                if current_page >= last_page:
                    current_page = last_page
                    self.warning_msg = "You are currenly on the last page"
                else:
                    current_page += 1
            elif action == 'p' or action == "previous":
                if current_page > 1:
                    current_page -= 1
                else:
                    current_page = 1
                    self.warning_msg = "You are currenly on the first page"
            elif action == 's' or action == "select":
                contract_id = input("Select contract by ID: ").lower()
                if contract_id == 'q':
                    break
                contract = self.logic.get_contract_by_id(contract_id)
                if contract is None:
                    self.warning_msg = "contract not found"
                else:
                    self.contract(contract_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single contract
    def contract(self, contract_id):
        while True:
            contract = self.logic.get_contract_by_id(contract_id)
            self.printer.header("View contract")
            print("ID:\t\t\t\t{}\nCustomer:\t\t\t\t{}\nVehicle:\t\t\t\t{}\nVehicle status:\t\t{}\nEmployee:\t\t\t{}\nLocation:\t\t\t{}\nDate from:\t\t\t{}\nDate to:\t\t\t{}\nContract date:\t\t\t{}\nContract status:\t\t\t{}\nPickup Date:\t\t\t{}\nDropoff date:\t\t\t{}\nTotal:\t\t\t{}\n".format(contract_id, self.logic.get_customer_by_id(contract.customer_id), self.logic.get_vehicle_by_id(contract.vehicle_id), contract.vehicle_status, self.logic.get_employee_by_id(contract.employee_id), self.logic.get_location_by_id(contract.location_id), contract.date_from, contract.date_to, contract.contract_date, contract.contract_status, contract.pickup_date, contract.dropoff_date, contract.total))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(contract_id)
            elif action == 'd' or action == 'delete':
                if self.delete(contract_id):
                    self.success_msg = "Contract has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"
    
    # Prints out table of contract
    def print(self, contracts, start, end, current_page, last_page):
        if len(contracts) > 0:
            print("|{:^4}|{:^15}|{:^15}|{:^20}|{:^15}|{:^30}|{:^15}|{:^15}|{:^15}|{:^20}|{:^15}|{:^15}|{:^10}|".format("ID", "Customer", "Vehicle", "Vehicle status", "Employee", "Location", "Date from", "Date to", "Contract date", "Contract status", "Pickup date", "Dropoff date", "Total"))
            print('-' * 218)
            for i in range(start, end):
                print("|{:^4}|{:^15}|{:^15}|{:^20}|{:^15}|{:^30}|{:^15}|{:^15}|{:^15}|{:^20}|{:^15}|{:^15}|{:^10}|".format(contracts[i].id, self.logic.get_customer_by_id(contracts[i].customer_id).__str__(), self.logic.get_vehicle_by_id(contracts[i].vehicle_id).__str__(), contracts[i].vehicle_status, contracts[i].employee_id, self.logic.get_location_by_id(contracts[i].location_id).__str__(), contracts[i].date_from, contracts[i].date_to, contracts[i].contract_date, contracts[i].contract_status, contracts[i].pickup_date, contracts[i].dropoff_date, contracts[i].total))
            print("{:^212}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No contracts found"
  

    def edit(self, contract_id):
        customer_id_page = 1
        vehicle_id_page = 1
        location_id_page = 1
        role_page = 1
        while True:
            contract = self.logic.get_contract_by_id(contract_id)
            update = {}
            self.printer.header("Edit contract")
            print(f"ID:\t\t\t\t{contract_id}\nCustomer:\t\t\t\t{self.logic.get_customer_by_id(contract.customer_id)}\nVehicle:\t\t\t\t{self.logic.get_vehicle_by_id(contract.vehicle_id)}\nLocation:\t\t\t{self.logic.get_location_by_id(contract.location_id)}\nDate from:\t\t\t{contract.date_from}\nDate to:\t\t\t{contract.date_to}\nContract status:\t\t\t{contract.contract_status}\nPickup date:\t\t\t{contract.pickup_date}\nDropoff date:\t\t\t{contract.dropoff_date}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            
            self.printer.new_line()
            self.printer.print_options(['Edit customer', 'Edit vehicle', 'Edit location', 'Edit date from', 'Edit date to', 'Edit contract status', 'Edit pick up date', 'Edit drop off date'])
            self.printer.new_line()
            self.notification()
            while True:
                action = input("Choose an option: ").lower()
                data = None
                try:
                    if action == "q":
                        return
                    elif action == "1":
                        while True:
                            customers = self.logic.get_all_customers()
                            available_customers = [[customer.id, customer] for customer in customers]
                            data = self.input.get_option("customer", available_customers, current_page = customer_id_page, warning_msg = self.warning_msg)
                            if data[0] == True:
                                update["customer_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                customer_id_page = data[2]                                
                    elif action == "2":
                        while True:
                            vehicles = self.logic.get_all_vehicles()
                            available_vehicles = [[vehicle.id, vehicle] for vehicle in vehicles]
                            data = self.input.get_option("vehicle", available_vehicles, current_page = vehicle_id_page, warning_msg = self.warning_msg)
                            if data[0]:
                                update["vehicle_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "3":
                        while True:
                            locations = self.logic.get_all_locations()
                            available_locations = [[location.id, location] for location in locations]
                            data = self.input.get_option("location", available_locations, current_page = location_id_page, warning_msg = self.warning_msg)
                            if data[0] == True:
                                update["location_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                location_id_page = data[2]
                    elif action == "4":
                        while True:
                            data = self.input.get_input("Date from", ["required", "date"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["date_from"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "5":
                        while True:
                            data = self.input.get_input("Date to", ["required", "date"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["date_to"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "6":
                        while True:
                            data = self.input.get_option("Contract status:", ["Open", "Closed", "Invalid"], current_page = role_page, warning_msg = self.warning_msg)
                            if data[0]:
                                update["contract_status"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "7":
                        while True:
                            data = self.input.get_input("Pick up date", ["required", "date"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["pickup_date"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "8":
                        while True:
                            data = self.input.get_input("Drop off date", ["required", "date"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["dropoff_date"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    else:
                        self.warning_msg = "Please select available option"
                    if(len(update) > 0):
                        self.logic.update_contract(contract_id, update)
                        self.success_msg = "contract has been modified"
                    break
                except ValueError:
                    break

    # Delete contract
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this contract? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_contract(id)
            return True
        return False

    # Outputs warnings and success messages
    def notification(self):
        if not self.warning_msg == "":
            self.printer.print_warning(self.warning_msg)
            self.warning_msg = ""
        elif not self.success_msg == "":
            self.printer.print_success(self.success_msg)
            self.success_msg = ""
        else:
            self.printer.new_line()