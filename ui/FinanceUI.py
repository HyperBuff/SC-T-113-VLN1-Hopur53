#Logic
from logic.MainLogic import MainLogic
#Models
from models.Location import Location
from models.Contract import Contract
#UI
from ui.PrinterUI import PrinterUI
from ui.InputUI import InputUI

class FinanceUI:
    #initialize
    def __init__(self, employee_id, employee_role):
        
        self.items_per_page = 10

        self.employee_id = employee_id
        self.employee_role = employee_role

        self.logic = MainLogic()

        self.printer = PrinterUI()
        self.input = InputUI()

        self.success_msg = ""
        self.warning_msg = ""

        self.menu()

    #Menu Options
    def menu_options(self):
        if self.employee_role.lower() == "admin":
            return {
                "View overview": self.overview,
                "View invoices": self.invoice
            }
        elif self.employee_role.lower() == "financial":
            return {
                "View overview": self.overview,
                "View invoices": self.invoice
            }

    def menu(self):
        while True:
            menu_options = self.menu_options()
            self.printer.header("Finance Menu")
            self.printer.print_menu_options(menu_options)
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                self.overview()
            elif action == '2':
                self.invoice()
            elif action == 'q':
                break
            try:
                list(menu_options.values())[int(action)-1]()
            except:
                self.warning_msg = "Please select available option"

    def overview(self):
        while True:
            self.printer.header("Overview Menu")
            self.printer.print_options(['Income overview', 'Utilization overview', 'Invoice overview'])
            self.printer.new_line(3)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                self.income_overview()
            elif action == '2':
                self.utilization_overview()
            elif action == '3':
                self.invoice_overview()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"


    def invoice(self):
        while True:
            self.printer.header("Invoice Menu")
            self.printer.print_options(['Print invoice', 'Unpaid invoices'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                self.view_invoices()
            elif action == '2':
                self.unpaid_invoice()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    #Overview Functions
    def income_overview(self):
        while True:
            self.printer.header("Income overview menu")
            self.printer.print_options(['Branch Income', 'Vehicle Type Income'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                self.branch_report()
            elif action == '2':
                self.vehicle_type_report()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    def utilization_overview(self):
        while True:
            vehicles = self.logic.get_all_vehicles()
            vehicles_dict = self.create_utilazation_report(vehicles)
            self.printer.header("Utilization Overview")
            self.print_utilazation_report(vehicles_dict)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("Input: ").lower()
            if action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    def branch_report(self):
        try:
            while True:
                while True:
                    date_1 = self.input.get_input("date from", ["required", "date"], warning_msg = self.warning_msg)
                    if date_1[0]:
                        date_1 = date_1[1]
                        break
                    else:
                        self.printer.print_warning(date_1[1])
                while True:
                    date_2 = self.input.get_input("date from", ["required", "date"], warning_msg = self.warning_msg)
                    if date_2[0]:
                        date_2 = date_2[1]
                        break
                    else:
                        self.printer.print_warning(date_2[1])

                contracts = self.logic.filter_contracts({"date": [date_1, date_2]})
                contract_dict = self.create_branch_report(contracts)
                self.printer.header("Branch Report")
                print("\n".join("\t{:^20} {:^20}".format(self.logic.get_location_by_id(k).country, v) for k, v in contract_dict.items()))
                self.printer.new_line()
                self.printer.print_fail("Press q to go back")
                self.notification()
                action = input("Input: ").lower()
                if action == 'q':
                    break
                else:
                    self.warning_msg = "Please select available option"
        except ValueError:
            return


    def vehicle_type_report(self):
        try:
            while True:
                while True:
                    date_1 = self.input.get_input("date from", ["required", "date"], warning_msg = self.warning_msg)
                    if date_1[0]:
                        date_1 = date_1[1]
                        break
                    else:
                        self.printer.print_warning(date_1[1])
                while True:
                    date_2 = self.input.get_input("date from", ["required", "date"], warning_msg = self.warning_msg)
                    if date_2[0]:
                        date_2 = date_2[1]
                        break
                    else:
                        self.printer.print_warning(date_2[1])

                contracts = self.logic.filter_contracts({"date": [date_1, date_2]})
                contract_dict = self.create_vehicletype_report(contracts)
                self.printer.header("Vehicle Type Report")
                print("\n".join("\t{:^20} {:^20}".format(k, v) for k, v in contract_dict.items()))
                self.printer.new_line()
                self.printer.print_fail("Press q to go back")
                self.notification()
                action = input("Input: ").lower()
                if action == 'q':
                    break
                else:
                    self.warning_msg = "Please select available option"
        except ValueError:
            return

    def invoice_overview(self, created = False):
        current_page = 1
        while True:
            try:
                while True:
                    date_1 = self.input.get_input("date from", ["required", "date"], warning_msg = self.warning_msg)
                    if date_1[0]:
                        date_1 = date_1[1]
                        break
                    else:
                        self.printer.print_warning(date_1[1])
                while True:
                    date_2 = self.input.get_input("date to", ["required", "date"], warning_msg = self.warning_msg)
                    if date_2[0]:
                        date_2 = date_2[1]
                        break
                    else:
                        self.printer.print_warning(date_2[1])
            except ValueError:
                return

            contracts = self.logic.filter_contracts({"date": [date_1, date_2]})
            contracts_count = len(contracts)
            last_page = int(contracts_count / self.items_per_page) + (contracts_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else contracts_count

            self.printer.header("Invoice Overview")
            self.print_invoice_overview(contracts, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("(N)ext page / (P)revious page: ").lower()

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
            else:
                self.warning_msg = "Please select available option"
  

    #Invoice Functions
    def view_invoices(self, created = False):
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

            self.printer.header("View Invoices")
            self.print(contracts, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("(N)ext page / (P)revious page / (S)elect Invoice: ").lower()

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
                contract_id = input("Select invoice by ID: ").lower()
                if contract_id == 'q':
                    break
                contract = self.logic.get_contract_by_id(contract_id)
                if contract is None:
                    self.warning_msg = "contract not found"
                else:
                    self.print_invoice(contract_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single invoice
    def print_invoice(self, contract_id):
        while True:
            contract = self.logic.get_contract_by_id(contract_id)
            self.printer.header("Invoice")
            print("ID:{}\nCustomer:\t{}\nContract date:\t\t{}\nContract status:\t{}\nTotal:\t\t\t{}\nPaid:\t\t\t{}\n".format(contract_id, self.logic.get_customer_by_id(contract.customer_id), contract.contract_date, contract.contract_status, contract.total, contract.paid))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("Select Option: ").lower()
            if action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    # Prints out all Unpaid Contracts
    def unpaid_invoice(self, created = False):
        current_page = 1
        try:
            while True:
                while True:
                    date_1 = self.input.get_input("date from", ["required", "date"], warning_msg = self.warning_msg)
                    if date_1[0]:
                        date_1 = date_1[1]
                        break
                    else:
                        self.printer.print_warning(date_1[1])
                while True:
                    date_2 = self.input.get_input("date to", ["required", "date"], warning_msg = self.warning_msg)
                    if date_2[0]:
                        date_2 = date_2[1]
                        break
                    else:
                        self.printer.print_warning(date_2[1])

                contracts = self.logic.filter_contracts({"date": [date_1, date_2], "contract_status": "open"})
                contracts_count = len(contracts)
                last_page = int(contracts_count / self.items_per_page) + (contracts_count % self.items_per_page > 0)
                if current_page > last_page:
                    current_page = last_page
                if created == True:
                    current_page = last_page
                    created = False
                start = (current_page - 1) * self.items_per_page
                end = start + 10 if not current_page == last_page else contracts_count

                self.printer.header("Unpaid Contract")
                self.print(contracts, start, end, current_page, last_page)
                self.printer.new_line()
                self.printer.print_fail("Press q to go back")
                self.notification()

                action = input("(N)ext page / (P)revious page / (S)elect Invoice: ").lower()

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
                        self.print_invoice(contract_id)
                else:
                    self.warning_msg = "Please select available option"
        except ValueError:
            return


    # Prints out table of contract
    def print(self, contracts, start, end, current_page, last_page):
        if len(contracts) > 0:
            print("|{:^4}|{:^40}|{:^25}|{:^15}|{:^27}|{:^15}|{:^15}|{:^15}|{:^20}|{:^15}|{:^15}|{:^10}|{:^10}|".format("ID", "Customer", "Vehicle", "Employee", "Location", "Date from", "Date to", "Contract Date", "Contract status", "Pickup date", "Dropoff date", "Total", "Paid"))
            print('-' * 240)
            for i in range(start, end):
                print("|{:^4}|{:^40}|{:^25}|{:^15}|{:^27}|{:^15}|{:^15}|{:^15}|{:^20}|{:^15}|{:^15}|{:^10}|{:^10}|".format(contracts[i].id, self.logic.get_customer_by_id(contracts[i].customer_id).__str__(), self.logic.get_vehicle_by_id(contracts[i].vehicle_id).__str__(), self.logic.get_employee_by_id( contracts[i].employee_id).__str__(), self.logic.get_location_by_id(contracts[i].location_id).__str__(), contracts[i].date_from, contracts[i].date_to, contracts[i].contract_date, contracts[i].contract_status, contracts[i].pickup_date, contracts[i].dropoff_date, contracts[i].total, contracts[i].paid))
            print("{:^240}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No contracts found"
    
    def print_invoice_overview(self, contracts, start, end, current_page, last_page):
        if len(contracts) > 0:
            print("|{:^5}|{:^35}|{:^10}|{:^10}|".format("ID", "Customer", "Total", "Paid"))
            print('-' * 65)
            for i in range(start, end):
                print("|{:^5}|{:^35}|{:^10}|{:^10}|".format(contracts[i].id, self.logic.get_customer_by_id(contracts[i].customer_id).__str__(), contracts[i].total, contracts[i].paid))
            print("{:^213}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No Invoices found"

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


    def create_branch_report(self, contracts):
        results = {}
        for contract in contracts:
            if contract.location_id not in results:
                results[contract.location_id] = []
            results[contract.location_id].append(int(contract.paid))
        updated_dict = {location: sum(amount) for location, amount in results.items()}
        return updated_dict


    def create_vehicletype_report(self, contracts):
        results = {}
        results2 = {}
        results3 = {}
        for contract in contracts:
            if contract.vehicle_id not in results:
                results[contract.vehicle_id] = []
            results[contract.vehicle_id].append(int(contract.paid))
        updated_dict = {vehicle: sum(amount) for vehicle, amount in results.items()}
        for key, value in updated_dict.items():
            if self.logic.get_vehicle_by_id(key).vehicle_type_id not in results2:
                results2[self.logic.get_vehicle_by_id(key).vehicle_type_id] = []
            results2[self.logic.get_vehicle_by_id(key).vehicle_type_id].append(value)
            updated_dict2 = {vt_id: sum(amount) for vt_id, amount in results2.items()}
        for key1, value1 in updated_dict2.items():
            if self.logic.get_vehicletype_by_id(key1).name not in results2:
                results3[self.logic.get_vehicletype_by_id(key1).name] = []
            results3[self.logic.get_vehicletype_by_id(key1).name].append(value1)
            updated_dict3 = {vt_id: sum(amount) for vt_id, amount in results3.items()}
        return updated_dict3

    def create_utilazation_report(self, vehicles):
            results = {}
            for vehicle in vehicles:
                if vehicle.location_id not in results:
                    results[vehicle.location_id] = []
                results[vehicle.location_id].append(vehicle.vehicle_type_id)
            return results

    def print_utilazation_report(self, vehicles_dict):
        for key, value in vehicles_dict.items():
            my_dict = {self.logic.get_vehicletype_by_id(i).name:value.count(i) for i in value}
            print(self.logic.get_location_by_id(key).country)
            print("\n".join("\t{}: {}".format(k, v) for k, v in my_dict.items()))