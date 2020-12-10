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

from ui.CustomerUI import CustomerUI



class ContractUI:

    def __init__(self, employee_id, employee_role):
        
        self.items_per_page = 10
        self.employee_id = employee_id
        self.employee_role = employee_role

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
        paid = 0
        
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
                    vehicle = self.logic.get_vehicle_by_id(vehicle_id)
                    location_id = vehicle.location_id

                    date_format = "%d/%m/%Y"

                    days = datetime.strptime(date_to, date_format) - datetime.strptime(date_from, date_format)
                    total = (int(days.days) + 1) * int(self.logic.get_vehicletype_by_id(vehicle.vehicle_type_id).rate)

                    print(total)
                    r = input("amount")

                    new_contract = Contract(customer_id,vehicle_id,employee_id,location_id,date_from,date_to,contract_date,contract_status,pickup_date,dropoff_date,total,paid)
                    confirmation = input("Are you sure you want to create this contract? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_contract(new_contract)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break
    
    def menu_options(self):
        if self.employee_role.lower() == "admin":
            return {
                "Create a contract": self.create,
                "View contracts": self.view,
                "Vehicle pick up": self.pick_up,
                "Return vehicle": self.drop_off,
                "Pay contract": self.pay_contract
            }
        elif self.employee_role.lower() == "delivery":
            return {
                "View contracts": self.view,
                "Deliver vehicle": self.pick_up,
                "Return vehicle": self.drop_off
            }
        elif self.employee_role.lower() == "booking":
            return {
                "Create a contract": self.create,
                "View contracts": self.view
            }

    
    # Prints out contract's menu
    def menu(self):
        while True:
            menu_options = self.menu_options()
            self.printer.header("Contracts Menu")
            self.printer.print_menu_options(menu_options)
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            if action == 'q':
                break
            try:
                list(menu_options.values())[int(action)-1]()
            except:
                self.warning_msg = "Please select available option"

    def pick_up(self):
        contracts_page = 1
        while True:
            location = self.logic.get_employee_by_id(self.employee_id).location_id
            contracts = self.logic.filter_contracts({"location": location, "status": "open", "pickup" : False})
            self.printer.header("Deliver vehicle")
            self.printer.print_fail("Press q to go back")
            self.notification()
            self.printer.new_line()
            available_contracts = [[contract.id, self.logic.get_customer_by_id(contract.customer_id)] for contract in contracts]
            if len(available_contracts) > 0:
                while True:
                    data = self.input.get_option("customer", available_contracts, current_page = contracts_page, warning_msg = self.warning_msg)
                    self.notification()
                    if data[0] == True:
                        contract_id = data[1]
                        break
                    else:
                        self.warning_msg = data[1]
                        contracts_page = data[2]
                    
                while True:

                    self.printer.header("Deliver vehicle")

                    contract = self.logic.get_contract_by_id(contract_id)
                    customer = self.logic.get_customer_by_id(contract.customer_id)
                    vehicle = self.logic.get_vehicle_by_id(contract.vehicle_id)
                    vehicletype = self.logic.get_vehicletype_by_id(vehicle.vehicle_type_id)

                    print(f"Name:\t\t\t\t{customer.name}\nSocial security number:\t\t{customer.ssn}\nPhone:\t\t\t\t{customer.phone}\nEmail:\t\t\t\t{customer.email}\n")
                    print(f"Manufacturer:\t\t\t{vehicle.manufacturer}\nModel:\t\t\t\t{vehicle.model}\nVehicle type:\t\t\t{vehicletype.name}\nRate:\t\t\t\t{vehicletype.rate}\nManufacture year:\t\t{vehicle.man_year}\nColor:\t\t\t\t{vehicle.color}\nLicence needed:\t\t\t{vehicle.licence_type}\n")
                    print(f"Delivery date:\t\t\t{contract.date_from}\nReturn date:\t\t\t{contract.date_to}\n")

                    self.printer.print_fail("Press q to go back")
                    self.notification()

                    action = input("(D)eliver vehicle: ").lower()
                    if action == 'q':
                        break
                    elif action == 'd' or action == "deliviery":
                        confirmation = input("Are you sure you want to deliver this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                        if confirmation == 'y':
                            self.logic.contract_set_pickup(contract_id, self.input.get_date())
                            self.success_msg = "Vehicle has been delivered successfully"
                            break
                    else:
                        self.warning_msg = "Please select available option"
            else:
                print("No delivery scheduled for your location")
                self.printer.new_line()
                self.notification()
                action = input("Choose an option: ").lower()
                if action == 'q':
                    return
                else:
                    self.warning_msg = "Please select available option"

    def drop_off(self):
        contracts_page = 1
        while True:
            location = self.logic.get_employee_by_id(self.employee_id).location_id
            contracts = self.logic.filter_contracts({"location": location, "status": "open", "pickup" : True, "dropoff" : False})
            self.printer.header("Return vechicle")
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            available_contracts = [[contract.id, self.logic.get_customer_by_id(contract.customer_id)] for contract in contracts]
            if len(available_contracts) > 0:
                while True:
                    data = self.input.get_option("customer", available_contracts, current_page = contracts_page, warning_msg = self.warning_msg)
                    if data[0] == True:
                        contract_id = data[1]
                        break
                    else:
                        self.warning_msg = data[1]
                        contracts_page = data[2]
                
                while True:

                    self.printer.header("Return vechicle")

                    contract = self.logic.get_contract_by_id(contract_id)
                    customer = self.logic.get_customer_by_id(contract.customer_id)
                    vehicle = self.logic.get_vehicle_by_id(contract.vehicle_id)
                    vehicletype = self.logic.get_vehicletype_by_id(vehicle.vehicle_type_id)

                    print(f"Name:\t\t\t\t{customer.name}\nSocial security number:\t\t{customer.ssn}\nPhone:\t\t\t\t{customer.phone}\nEmail:\t\t\t\t{customer.email}\n")
                    print(f"Manufacturer:\t\t\t{vehicle.manufacturer}\nModel:\t\t\t\t{vehicle.model}\nVehicle type:\t\t\t{vehicletype.name}\nRate:\t\t\t\t{vehicletype.rate}\nManufacture year:\t\t{vehicle.man_year}\nColor:\t\t\t\t{vehicle.color}\nLicence needed:\t\t\t{vehicle.licence_type}\n")
                    print(f"Delivery date:\t\t\t{contract.date_from}\nReturn date:\t\t\t{contract.date_to}\n")
                    print(f"Amount paid:\t\t\t{contract.paid}\nTotal amount:\t\t\t{contract.total}\nAmount due:\t\t\t{contract.amount_due()}\n")

                    self.printer.print_fail("Press q to go back")
                    self.notification()

                    action = input("(R)eturn vechicle: ").lower()
                    if action == 'q':
                        break
                    elif action == 'r' or action == "return":
                        confirmation = input("Are you sure you want to return this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                        if confirmation == 'y':
                            self.logic.contract_set_dropoff(contract_id, self.input.get_date())
                            self.success_msg = "Vehicle has been returned successfully"
                            break
                    else:
                        self.warning_msg = "Please select available option"

            else:
                print("No return scheduled for your location")
                self.printer.new_line()
                self.notification()
                action = input("Choose an option: ").lower()
                if action == 'q':
                    return
                else:
                    self.warning_msg = "Please select available option"

    

    def pay_contract(self):
        contracts_page = 1
        while True:
            location = self.logic.get_employee_by_id(self.employee_id).location_id
            contracts = self.logic.filter_contracts({"location": location, "status": "open"})
            self.printer.header("Pay vechicle")
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            available_contracts = [[contract.id, self.logic.get_customer_by_id(contract.customer_id)] for contract in contracts]
            if len(available_contracts) > 0:
                while True:
                    data = self.input.get_option("contract", available_contracts, current_page = contracts_page, warning_msg = self.warning_msg)
                    if data[0] == True:
                        contract_id = data[1]
                        break
                    else:
                        self.warning_msg = data[1]
                        contracts_page = data[2]
                
                while True:

                    self.printer.header("Pay contract")

                    contract = self.logic.get_contract_by_id(contract_id)
                    customer = self.logic.get_customer_by_id(contract.customer_id)
                    vehicle = self.logic.get_vehicle_by_id(contract.vehicle_id)
                    vehicletype = self.logic.get_vehicletype_by_id(vehicle.vehicle_type_id)

                    print(f"Name:\t\t\t\t{customer.name}\nSocial security number:\t\t{customer.ssn}\nPhone:\t\t\t\t{customer.phone}\nEmail:\t\t\t\t{customer.email}\n")
                    print(f"Manufacturer:\t\t\t{vehicle.manufacturer}\nModel:\t\t\t\t{vehicle.model}\nVehicle type:\t\t\t{vehicletype.name}\nRate:\t\t\t\t{vehicletype.rate}\nManufacture year:\t\t{vehicle.man_year}\nColor:\t\t\t\t{vehicle.color}\nLicence needed:\t\t\t{vehicle.licence_type}\n")
                    print(f"Delivery date:\t\t\t{contract.date_from}\nReturn date:\t\t\t{contract.date_to}\n")
                    print(f"Actual delivery date:\t\t\t{contract.pickup_date}\nActual return date:\t\t\t{contract.dropoff_date}\n")
                    print(f"Amount paid:\t\t\t{contract.paid}\nTotal amount:\t\t\t{contract.total}\nAmount due:\t\t\t{contract.amount_due()}\n")

                    self.printer.print_fail("Press q to go back")
                    self.notification()

                    action = input("(C)lose contract / (P)ay partial: ").lower()

                    if action == 'q':
                        break
                    elif action == 'c' or action == "close":
                        amount = contract.amount_due()
                        confirmation = input("Are you sure you want to add {} to this contract? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ".format(amount)).lower()
                        if confirmation == 'y':
                            self.logic.pay_to_contract(contract_id, amount)
                            break
                    elif action == 'p' or action == "pay":
                        amount = input("Enter amount between (1 - {}): ".format(contract.amount_due()))
                        confirmation = input("Are you sure you want to add {} to this contract? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ".format(amount)).lower()
                        if confirmation == 'y':
                            self.logic.pay_to_contract(contract_id, amount)
                            break
                    else:
                        self.warning_msg = "Please select available option"

                    

            else:
                print("No open contracts for your location")
                self.printer.new_line()
                self.notification()
                action = input("Choose an option: ").lower()
                if action == 'q':
                    return
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
            print("ID:\t\t\t\t{}\nCustomer:\t\t\t\t{}\nVehicle:\t\t\t\t{}\nEmployee:\t\t\t{}\nLocation:\t\t\t{}\nDate from:\t\t\t{}\nDate to:\t\t\t{}\nContract date:\t\t\t{}\nContract status:\t\t\t{}\nPickup Date:\t\t\t{}\nDropoff date:\t\t\t{}\nTotal:\t\t\t{}\nPaid:\t\t\t{}\n".format(contract_id, self.logic.get_customer_by_id(contract.customer_id), self.logic.get_vehicle_by_id(contract.vehicle_id), self.logic.get_employee_by_id(contract.employee_id), self.logic.get_location_by_id(contract.location_id), contract.date_from, contract.date_to, contract.contract_date, contract.contract_status, contract.pickup_date, contract.dropoff_date, contract.total, contract.paid))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(E)dit / (I)nvalidate / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(contract_id)
            elif action == 'd' or action == 'delete':
                if self.delete(contract_id):
                    self.success_msg = "Contract has been deleted"
                    break
            elif action == 'i' or action == 'invalidate':
                if self.invalidate(contract_id):
                    self.success_msg = "Contract has been invalidated"
                    break
            else:
                self.warning_msg = "Please select available option"
    
    # Prints out table of contract
    def print(self, contracts, start, end, current_page, last_page):
        if len(contracts) > 0:
            print("|{:^4}|{:^15}|{:^20}|{:^15}|{:^20}|{:^15}|{:^15}|{:^15}|{:^20}|{:^15}|{:^15}|{:^10}|{:^10}|".format("ID", "Customer", "Vehicle", "Employee", "Location", "Date from", "Date to", "Contract Date", "Contract status", "Pickup date", "Dropoff date", "Total", "Paid"))
            print('-' * 213)
            for i in range(start, end):
                print("|{:^4}|{:^15}|{:^20}|{:^15}|{:^20}|{:^15}|{:^15}|{:^15}|{:^20}|{:^15}|{:^15}|{:^10}|{:^10}|".format(contracts[i].id, self.logic.get_customer_by_id(contracts[i].customer_id).__str__(), self.logic.get_vehicle_by_id(contracts[i].vehicle_id).__str__(), self.logic.get_employee_by_id( contracts[i].employee_id).__str__(), self.logic.get_location_by_id(contracts[i].location_id).__str__(), contracts[i].date_from, contracts[i].date_to, contracts[i].contract_date, contracts[i].contract_status, contracts[i].pickup_date, contracts[i].dropoff_date, contracts[i].total, contracts[i].paid))
            print("{:^213}".format("Page {} of {}".format(current_page, last_page)))
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
                                date_format = "%d/%m/%Y"
                                days = datetime.strptime(contract.date_to, date_format) - datetime.strptime(contract.date_to, date_format)
                                total = int(days.days) * int(self.logic.get_vehicletype_by_id(data[1]).rate)
                                update["total"] = total
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
                        self.success_msg = "Contract has been modified"
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

    def invalidate(self, contract_id):
        confirmation = input("Are you sure you want to invalidate this contract? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.update_contract(contract_id, {"contract_status": "Invalid"})
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