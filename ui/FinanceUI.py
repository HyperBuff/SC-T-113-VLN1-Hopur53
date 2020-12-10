#Logic
from logic.MainLogic import MainLogic
#Models
from models.Location import Location
from models.Contract import Contract
#UI
from ui.PrinterUI import PrinterUI
from ui.InputUI import InputUI

class FinanceUI:

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

    def menu_options(self):
        if self.employee_role.lower() == "admin":
            return {
                "View overview": self.Overview,
                "View invoices": self.Invoice
            }
        elif self.employee_role.lower() == "financial":
            return {
                "View overview": self.Overview,
                "View invoices": self.Invoice
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
                self.Overview()
            elif action == '2':
                self.Invoice()
            elif action == 'q':
                break
            try:
                list(menu_options.values())[int(action)-1]()
            except:
                self.warning_msg = "Please select available option"

    def Overview(self):
        while True:
            self.printer.header("Overview Menu")
            self.printer.print_options(['Branch Overview', 'Utilization Overview', 'Invoice Overview'])
            self.printer.new_line(3)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                self.income_overview()
            elif action == '2':
                pass
            elif action == '3':
                pass
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"


    def Invoice(self):
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
            print("ID:\t\t\t\t{}\nCustomer:\t\t\t{}\nContract date:\t\t\t{}\nContract status:\t\t{}\nTotal:\t\t\t\t{}\nPaid:\t\t\t\t{}\n".format(contract_id, self.logic.get_customer_by_id(contract.customer_id), contract.contract_date, contract.contract_status, contract.total, contract.paid))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(P)rint invoice").lower()
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
                    date_2 = self.input.get_input("date from", ["required", "date"], warning_msg = self.warning_msg)
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
            print("|{:^4}|{:^15}|{:^20}|{:^15}|{:^20}|{:^15}|{:^15}|{:^15}|{:^20}|{:^15}|{:^15}|{:^10}|{:^10}|".format("ID", "Customer", "Vehicle", "Employee", "Location", "Date from", "Date to", "Contract Date", "Contract status", "Pickup date", "Dropoff date", "Total", "Paid"))
            print('-' * 213)
            for i in range(start, end):
                print("|{:^4}|{:^15}|{:^20}|{:^15}|{:^20}|{:^15}|{:^15}|{:^15}|{:^20}|{:^15}|{:^15}|{:^10}|{:^10}|".format(contracts[i].id, self.logic.get_customer_by_id(contracts[i].customer_id).__str__(), self.logic.get_vehicle_by_id(contracts[i].vehicle_id).__str__(), self.logic.get_employee_by_id( contracts[i].employee_id).__str__(), self.logic.get_location_by_id(contracts[i].location_id).__str__(), contracts[i].date_from, contracts[i].date_to, contracts[i].contract_date, contracts[i].contract_status, contracts[i].pickup_date, contracts[i].dropoff_date, contracts[i].total, contracts[i].paid))
            print("{:^213}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No contracts found"

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




        
