#Logic
from logic.MainLogic import MainLogic
#Models
from models.Location import Location
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


    def menu(self):
        while True:
            self.printer.header("Finance Menu")
            self.printer.print_options(['View overview', 'View invoices'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                self.Overview()
            elif action == '2':
                pass
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    def Overview(self):
        while True:
            self.printer.header("Overview Menu")
            self.printer.print_options(['View income', 'View vehicle utilization', 'View invoice'])
            self.printer.new_line(3)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                pass
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
            self.printer.print_options(['Print invoice', 'Unpaid Contracts'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                pass
            elif action == '2':
                pass
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"



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