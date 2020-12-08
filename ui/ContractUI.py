from logic.MainLogic import MainLogic
from models.Contract import Contract

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

    # Prints out contract's menu
    def menu(self):
        while True:
            self.printer.header("Contracts Menu")
            self.printer.print_options(['Create an contract', 'View contracts', 'Print invoice'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                if self.create():
                    self.success_msg = "New contract has been created"
                    self.view(True)
            elif action == '2':
                self.view()
            elif action == '3':
                self.print_invoice()
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
            self.print_contracts(contracts, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()

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
                contract_id = input("Select contract by ID: ")
                contract = self.logic.get_contract_by_id(contract_id)
                if contract is None:
                    self.warning_msg = "Contract not found"
                else:
                    self.select_contract(contract_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single contract
    def select_contract(self, contract_id):
        while True:
            contract = self.logic.get_contract_by_id(contract_id)
            self.printer.header("View contract")
            print("Id:\t\t\t\t{}\nName:\t\t\t\t{}\nSocial Security Number:\t\t{}\nPhone:\t\t\t\t{}\nEmail:\t\t\t\t{}\nAddress:\t\t\t{}\nVehicle Id:\t\t\t{}\nVehicle Status:\t\t\t{}\nEmployee Id:\t\t\t{}\nLocation ID:\t\t\t{}\nDate From:\t\t\t{}\nDate To:\t\t\t{}\nLoan date:\t\t\t{}\nLoan status:\t\t\t{}\nReturn date:\t\t\t{}\nTotal:\t\t\t\t{}\n".format(contract.id, contract.name, contract.ssn, contract.phone, contract.email, contract.address, contract.vehicle_id, contract.vehicle_status, contract.employee_id, contract.location_id, contract.date_from, contract.date_to, contract.loan_date, contract.loan_status, contract.return_date, contract.total))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(contract_id)
            elif action == 'd' or action == 'delete':
                if self.delete(contract_id):
                    self.success_msg = "contract has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"
            
    # Prints out table of contract
    def print_contracts(self, contracts, start, end, current_page, last_page):
        if len(contracts) > 0:
            print("|{:^6}|{:^15}|{:^15}|{:^15}|{:^24}|{:^18}|{:^13}|{:^18}|{:^11}|{:^13}|{:^10}|{:^10}|{:^10}|{:^15}|{:^15}|{:^10}|".format("ID", "Name", "Social security number", "Phone", "Email", "Address", "Vehicle Id", "Vehicle Status", "Employee Id", "Location ID", "Date from", "Date to", "Loan date", "Loan status", "Return date", "Total"))
            print('-' * 219)
            for i in range(start, end):
                print("|{:^6}|{:^15}|{:<15}|{:<15}|{:<24}|{:<18}|{:<13}|{:<18}|{:<11}|{:<13}|{:<10}|{:<10}|{:<10}|{:<15}|{:<15}|{:<10}|".format(contracts[i].id, contracts[i].name, contracts[i].ssn, contracts[i].phone, contracts[i].email, contracts[i].address, contracts[i].vehicle_id, contracts[i].vehicle_status, contracts[i].employee_id, contracts[i].location_id, contracts[i].date_from, contracts[i].date_to, contracts[i].loan_date, contracts[i].loan_status, contracts[i].return_date, contracts[i].total))
            print("{:^216}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No contracts found"

    # Create contract
    def create(self):
        self.printer.header("Add contract")
        self.printer.new_line()
        self.printer.print_fail("Press q to go back")
        self.printer.new_line()
        try:
            name = self.input.get_input("name")
            ssn = self.input.get_input("ssn")
            phone = self.input.get_input("phone", ["phone"])
            email = self.input.get_input("email", ["email"])
            address = self.input.get_input("address")

            date_from = self.input.get_input("date from", ["date"])
            date_to = self.input.get_input("date to", ["date"])

            vehicle_id = self.input.get_input("vehicle id")
            location_id = self.input.get_input("location")
            vehicle_status = self.input.get_input("vehicle status")

            loan_date = self.input.get_input("loan date", ["date"])
            return_date = self.input.get_input("return date", ["date"])

            total = self.input.get_input("total")
            loan_status = self.input.get_input("loan status")

            new_contract = Contract(name, ssn, phone, email, address, vehicle_id, vehicle_status, self.employee_id, location_id, date_from, date_to, loan_date, loan_status, return_date, total)
            self.logic.create_contract(new_contract)
            return True
        except ValueError:
            return False
       
    # Edit contract
    def edit(self, id):
        while True:
            updates = {}
            self.printer.header("Edit contract")
            self.printer.print_options(['Change name', 'Change phone', 'Change email', 'Change address', 'Edit date from', 'Edit date to', 'Edit vehicle id', 'Edit location', 'Edit vehicle status', 'Edit loan date', 'Edit return date', 'Edit total', 'Edit loan status'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == 'q':
                break
            elif action == '1':
                try:
                    name = self.input.get_input("name")
                    updates["name"] = name
                except ValueError:
                    break
            elif action == '2':
                try:
                    phone = self.input.get_input("phone", ["phone"])
                    updates["phone"] = phone
                except ValueError:
                    break
            elif action == '3':
                try:
                    email = self.input.get_input("email", ["email"])
                    updates["email"] = email
                except ValueError:
                    break
            elif action == '4':
                try:
                    address = self.input.get_input("address")
                    updates["address"] = address
                except ValueError:
                    break
            elif action == '5':
                try:
                    date_from = self.input.get_input("date from")
                    updates["date_from"] = date_from
                except ValueError:
                    break
            elif action == '6':
                try:
                    date_to = self.input.get_input("date to")
                    updates["date_to"] = date_to
                except ValueError:
                    break
            elif action == "7":
                try:
                    vehicle_id = self.input.get_input("vehicle id")
                    updates["vehicle_id"] = vehicle_id
                except ValueError:
                    break
            elif action == "8":
                try:
                    location = self.input.get_input("location")
                    updates["location"] = location
                except ValueError:
                    break
            elif action == "9":
                try:
                    vehicle_status = self.input.get_input("vehicle status")
                    updates["vehicle_status"] = vehicle_status
                except ValueError:
                    break
            elif action == "10":
                try:
                    loan_date = self.input.get_input("loan date")
                    updates["loan_date"] = loan_date
                except ValueError:
                    break
            elif action == "11":
                try:
                    return_date = self.input.get_input("return date")
                    updates["return_date"] = return_date
                except ValueError:
                    break
            elif action == "12":
                try:
                    total = self.input.get_input("total")
                    updates["total"] = total
                except ValueError:
                    break
            elif action == "13":
                try:
                    loan_status = self.input.get_input("loan status")
                    updates["loan_status"] = loan_status
                except ValueError:
                    break
            else:
                self.warning_msg = "Please select available option"

            if(len(updates) > 0):
                self.logic.update_contract(id, updates)
                self.success_msg = "{} has been modified".format(list(updates.keys())[0].capitalize())

    # Delete contract
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this contract? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_contract(id)
            return True
        return False

    # Outputs warnings and success messages
    def print_msg(self):
        if not self.warning_msg == "":
            self.printer.print_warning(self.warning_msg)
            self.warning_msg = ""
        elif not self.success_msg == "":
            self.printer.print_success(self.success_msg)
            self.success_msg = ""
        else:
            self.printer.new_line()

    def print_invoice(self):

        while True:
            contract_id = input("Enter contract ID: ")
            if contract_id == 'q':
                break
            else:
                contract = self.logic.get_contract_by_id(contract_id)
                self.printer.header("Invoice")
                print("\nId:\t\t\t\t{}\n\nName:\t\t\t\t{}\n\nSocial security number:\t\t{}\n\nEmail:\t\t\t\t{}\n\nAddress:\t\t\t{}\n\n".format(contract.id, contract.name, contract.ssn, contract.email, contract.address))

        
            
