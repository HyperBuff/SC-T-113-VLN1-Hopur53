from logic.MainLogic import MainLogic
from models.Customer import Customer
from models.Location import Location

from ui.PrinterUI import PrinterUI
from ui.InputUI import InputUI

class CustomerUI:

    def __init__(self):
        
        self.items_per_page = 10

        self.logic = MainLogic()

        self.printer = PrinterUI()
        self.input = InputUI()

        self.success_msg = ""
        self.warning_msg = ""

        self.menu()


    def create(self):
        counter = 0

        name = ""
        email = ""
        ssn = ""
        phone = ""
        address = ""
        postal = ""
        
        while True:
            self.printer.header("Create customer")
            print(f"Name:\t\t\t\t{name}\nEmail:\t\t\t\t{email}\nSocial security number:\t\t{ssn}\nMobile phone:\t\t\t{phone}\nAddress:\t\t\t{address}\nPostal code:\t\t\t{postal}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.notification()
            next_input = True
            data = None
            try:
                if counter == 0:
                    data = self.input.get_input("name", ["required"], warning_msg = self.warning_msg)  
                    if data[0]:
                        name = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 1:
                    data = self.input.get_input("address", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        address = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 2:
                    data = self.input.get_input("postal code", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        postal = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 3:
                    data = self.input.get_input("mobile phone", ["required", "ssn"], warning_msg = self.warning_msg)
                    if data[0]:
                        ssn = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 4:
                    data = self.input.get_input("phone", ["required", "phone"], warning_msg = self.warning_msg)
                    if data[0]:
                        phone = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 5:
                    data = self.input.get_input("email", ["required", "email"], warning_msg = self.warning_msg)
                    if data[0]:
                        email = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 6:
                    data = self.input.get_input("country", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        country = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter > 6:
                    new_customer = Customer(name, address, postal, ssn, phone, email, country)
                    confirmation = input("Are you sure you want to create this customer? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_customer(new_customer)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break

    # Prints out customer's menu
    def menu(self):
        while True:
            self.printer.header("Customers Menu")
            self.printer.print_options(['Create an customer', 'View customers'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                if self.create():
                    self.success_msg = "New customer has been created"
                    self.view(True)
            elif action == '2':
                self.view()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    # Prints out all customer
    def view(self, created = False):
        current_page = 1
        while True:   
            customers = self.logic.get_all_customers()
            customers_count = len(customers)
            last_page = int(customers_count / self.items_per_page) + (customers_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else customers_count

            self.printer.header("View customers")
            self.print(customers, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("(N)ext page / (P)revious page / (S)elect customer: ").lower()

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
                customer_id = input("Select customer by ID: ").lower()
                if customer_id == 'q':
                    break
                customer = self.logic.get_customer_by_id(customer_id)
                if customer is None:
                    self.warning_msg = "customer not found"
                else:
                    self.customer(customer_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single customer
    def customer(self, customer_id):
        while True:
            customer = self.logic.get_customer_by_id(customer_id)
            self.printer.header("View customer")
            print("ID:\t\t\t\t{}\nRole:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\nLocation:\t\t\t{}\n".format(customer_id, customer.role, customer.name, customer.email, customer.ssn, customer.phone, customer.homephone, customer.address, customer.postal, self.logic.get_location_by_id(customer.location_id)))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(customer_id)
            elif action == 'd' or action == 'delete':
                if self.delete(customer_id):
                    self.success_msg = "customer has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"
    
    # Prints out table of customer
    def print(self, customers, start, end, current_page, last_page):
        if len(customers) > 0:
            print("|{:^6}|{:^15}|{:^25}|{:^30}|{:^30}|{:^20}|{:^20}|{:^25}|".format("ID", "Name", "Email", "Social security number", "Phone", "Address", "Postal code", "Country"))
            print('-' * 170)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<25}|{:<30}|{:<30}|{:<20}|{:<20}|{:<25}|".format(customers[i].id, customers[i].name, customers[i].email, customers[i].ssn, customers[i].phone, customers[i].address, customers[i].postal, customers[i].country))
            print("{:^170}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No customers found"
  

    def edit(self, customer_id):
        location_id_page = 1
        role_page = 1
        while True:
            customer = self.logic.get_customer_by_id(customer_id)
            update = {}
            self.printer.header("Edit customer")
            print(f"ID:\t\t\t\t{customer_id}\nName:\t\t\t\t{customer.name}\nEmail:\t\t\t\t{customer.email}\nSocial security number:\t\t{customer.ssn}\nPhone:\t\t\t{customer.phone}\nAddress:\t\t\t{customer.address}\nPostal code:\t\t\t{customer.postal}\nCountry:\t\t\t{customer.country}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit email', 'Edit phone', 'Edit address', 'Edit postal code', 'Edit country'])
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
                            data = self.input.get_input("email", ["required", "email"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["email"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "2":
                        while True:
                            data = self.input.get_input("phone", ["required", "phone"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["phone"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "3":
                        while True:
                            data = self.input.get_input("address", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["homephone"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "4":
                        while True:
                            data = self.input.get_input("postal code", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["postal"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "5":
                        while True:
                            data = self.input.get_input("country", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["country"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    if(len(update) > 0):
                        self.logic.update_customer(customer_id, update)
                        self.success_msg = "customer has been modified"
                    break
                except ValueError:
                    break

    # Delete customer
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this customer? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_customer(id)
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