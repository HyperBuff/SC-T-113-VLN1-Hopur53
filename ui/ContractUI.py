import math

from logic.MainLogic import MainLogic
from models.Contract import Contract

from ui.PrinterUI import PrinterUI

class EmployeeUI:

        def __init__(self):
                self.logic = MainLogic()
                self.printer = PrinterUI()
                self.success_msg = ""
                self.warning_msg = ""

<<<<<<< HEAD
    # Prints out employee's menu
        def menu(self):
                while True:
                self.printer.header("Contracts Menu")
                self.printer.print_options(['Create an contracts', 'View contracts'])
                self.printer.new_line(2)
                self.printer.print_fail("Press q to go back")
                self.print_msg()
                action = input("Choose an option: ").lower()
                if action == '1':
                        if self.create():
                        self.success_msg = "New contract has been created"
                        self.view()
                elif action == '2':
                        self.view()
                elif action == 'q':
                        break
                else:
                        self.warning_msg = "Please select available option"

        def create(self):
                # self.header("Create New Contract")
                self.printer.header("Add employee")
                self.printer.new_line()
                self.printer.print_fail("Press q to go back")
                self.printer.new_line()
                
                print("Enter employee details:")

                while True :
                        name = input("\tFull name: ")
                        if name == 'q' :
                                return
                        if len(name) < 1 :
                                 self.printer.print_warning("Name must be at least 1 character")
                        else:
                                break

                while True :        
                        ssn = input("\tEnter social security number: ")
                        if ssn == 'q':
                                return
                        if len(ssn) < 1:
                                self.printer.print_warning("Social security number must be at least 1 character")
                        elif not self.logic.is_ssn_valid(ssn):
                                self.printer.print_warning("Social security number is not valid")
                        else:
                                break
                        
                while True:
                        email = input("\tEnter email: ")
                        if email == 'q':
                                return
                        if len(email) < 1:
                                self.printer.print_warning("Email must be at least 1 character")
                        elif not self.logic.is_email_valid(email):
                                self.printer.print_warning("Email is not valid")
                        else:
                                break
                
                while True:
                        phone = input("\tEnter mobile phone: ")
                        if phone == 'q':
                                return
                        if len(phone) < 1:
                                self.printer.print_warning("Mobile phone must be at least 1 character")
                        elif not self.logic.is_phone_number_valid(phone):
                                self.printer.print_warning("Phone number is not valid")
                        else:
                                break
                                
                while True:
                        address = input("\tEnter address: ")
                        if address == 'q':
                                return
                        if len(address) < 1:
                                self.printer.print_warning("Address must be at least 1 character")
                        else:
                                break
                        
                while True:
                        postal = input("\tEnter postal: ")
                        if postal == 'q':
                                return
                        if len(postal) < 1:
                                self.printer.print_warning("Postal must be at least 1 character")
                        else:
                                break

                while True :        
                        country_origin = input("\tEnter country of recidence: \n")
                        if country_origin ==  'q':
                                return
                        if len(country_origin) < 1:
                                self.printer.print_warning("Country of recidence must be at least 1 character")
                        else:
                                break   

                print ("Vehicle information\n")
                
                while True :
                        vehicle_id = input("\tVehicle chosen: ")
                        if vehicle_id ==  'q':
                                return
                        if len(vehicle_id) < 1:
                                self.printer.print_warning("Vehicle ID must be at least 1 character")
                        else:
                                break
                
                while True :
                        vehicle_type = input("\tEnter vehicle type")
                        if vehicle_id ==  'q':
                                return
                        if len(vehicle_id) < 1:
                                self.printer.print_warning("Vehicle type must be at least 1 character")
                        else:
                                break

                print ("\nRental information\n")
                print ('''\33[;34mPlease enter pick-up and drop-off time, use the format dd.mm.yyyy 
                and seperate date and time with a comma\33[;0m
                ''')
                #Þarf að gera rétt format villucheck
                date_from = input("\tEnter pick-up date: ")
                date_to = input("\tEnter drop-off date: ")
                rental_period = date_from + " - " + date_to
                print ("\t\t\33[;36mRental period: \33[;0m", rental_period) 
                
                while True : 
                        #Vantar format villucheck
                        contract_made = input ("\tDate of booking: ")
                        if contract_made == 'q' :
                                return
                        if len(contract_made) > 1 :
                                self.printer.print_warning("Date of booking must be at least 1 character")
                        else:
                                break
                
                while True : 
                        destination = input("\tCountry of rental: ")
                        if destination == 'q':
                                return
                        if len(destination) < 1:
                                self.printer.print_warning("Country of rental must be at least 1 character")
                        else :
                                break

                print("\n\n1. Print contract\n2. Modify Contract\n\33[;31mPress q to go back\33[;0m\n")
                action = input("\nChoose an option: ").lower() 

                if action == "1":
                        return print_contracts()
                if action == "2":
                        return edit(self,id)
                if action == "q":
                        return menu()

        # Prints out all employee
        def view(self, current_page = 1):

                while True:   
                        contracts = self.logic.get_all_contracts()
                        contract_count = len(contracts)
                        last_page = math.ceil(contract_count / self.items_per_page)
                        self.printer.header("View contracts")
                        start = (current_page - 1) * self.items_per_page
                        end = start + 10 if not current_page == last_page else contract_count
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
                                employee_id = input("Select contract by ID: ")
                                employee = self.logic.get_contract_by_id(contract_id)
                                if employee is None:
                                        self.warning_msg = "Contract not found"
                                else:
                                        self.select_contract(contract_id)
                        else:
                                self.warning_msg = "Please select available option"

        # Prints out single employee
        def select_contract(self, contract_id):
                while True:
                        contract = self.logic.get_contract_by_id(contract_id)
                        self.printer.header("View contract")
                        print("ID:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nVehicle ID:\t\t\t{}\nRental Period:\t\t\t\t{}\nCountry:\t\t\t\t{}".format(contract.id, contract.name, contract.email, vehicle.id, rental_period, contract.destination))
                        self.printer.new_line()
                        self.printer.print_fail("Press q to go back")
                        self.print_msg()
                        action = input("(E)dit / (D)elete: ").lower()
                        if action == 'q':
                                break
                        elif action == 'e' or action == 'edit':
                                self.edit(contract_id)
                        elif action == 'd' or action == 'delete':
                                self.delete(contract_id)
                                self.success_msg = "Contract has been deleted"
                                break
                        else:
                                self.warning_msg = "Please select available option"
                def edit(self, id):
                        while True:
                                updates = {}
                                self.printer.header("Edit employee")
                                self.printer.print_options(['Change role', 'Change email', 'Change mobile phone', 'Change home phone', 'Edit address', 'Edit postal code'])
                                self.printer.new_line(2)
                                self.printer.print_fail("Press q to go back")
                                self.print_msg()
                                action = input("Choose an option: ").lower()
                                if action == 'q':
                                        break
                                if action == '1':
                                        name = input("\tEnter name: ")
                                        while True:
                        
                                                if name == 'q':
                                                        break    
                                                if len(name) < 1:
                                                        self.printer.print_warning("Email must be at least 1 character")
                                                elif not self.logic.is_email_valid(name):
                                                        self.printer.print_warning("Email is not valid")
                                                else:
                                                        updates["name"] = name
                                elif action == '2':
                                        ssn = input("\tEnter social security number: ")
                                        while True:
                                                if ssn == 'q':
                                                        break
                                                if len(ssn) < 1:
                                                        self.printer.print_warning("Social security number must be at least 1 character")
                                                elif not self.logic.is_ssn_valid(ssn):
                                                        self.printer.print_warning("Social security number is not valid")
                                                        updates["ssn"] = ssn
                                                        break
                                elif action == '3':
                                        email = input("\tEnter email: ")
                                        while True:
                                                if email == 'q':
                                                        break
                                                if len(email) < 1:
                                                        self.printer.print_warning("Email must be at least 1 character")
                                                elif not self.logic.is_email_valid(email):
                                                        self.printer.print_warning("Email is not valid")
                                                else:
                                                        updates["email"] = email
                                                        break
                                elif action == '4':
                                        phone = input("\tEnter home phone: ")
                                        while True:
                                                if phone == 'q':
                                                        break
                                                if len(phone) < 1:
                                                        self.printer.print_warning("Mobile phone must be at least 1 character")
                                                elif not self.logic.is_phone_number_valid(phone):
                                                        self.printer.print_warning("Phone number is not valid")
                                                else:
                                                        updates["homephone"] = phone
                                                        break
                                elif action == '5':
                                        address = input("\tEnter address: ")
                                        while True:
                                                if address == 'q':
                                                        break
                                                if len(address) < 1:
                                                        self.printer.print_warning("Address must be at least 1 character")
                                                else:
                                                        updates["address"] = address
                                                        break
                                elif action == '6':
                                        postal = input("\tEnter postal: ")
                                        while True:
                                                if postal == 'q':
                                                        return
                                                if len(postal) < 1:
                                                        self.printer.print_warning("Postal must be at least 1 character")
                                                else:
                                                        updates["postal"] = postal
                                                        break
                                elif action == '7':
                                        country_origin = input("\tEnter country of recidence: \n")
                                        while True:
                                                if country_origin ==  'q':
                                                        return
                                                if len(country_origin) < 1:
                                                        self.printer.print_warning("Country of recidence must be atleast 1 character")
                                                else:
                                                        updates["country_origin"] = country_origin
                                                        break
                self.logic.update_employee(id, updates)
=======
        name = input("\tFull name: ")
        ssn = input("\tEnter ssn: ")
        email = input("\tEnter email: ")
        phone = input("\tEnter mobile phone: ")
        address = input("\tEnter adress: ")
        postal = input("\tEnter postal code: ")
        country_origin = input("\tEnter country of recidence: \n")
        
        print ("Vehicle information\n")
        vehicle_id = input("\tVehicle chosen: ") 
        vehicle_type = input("\tEnter vehicle type")

        print ("\nRental information\n")
        print ('''\33[;34mPlease enter pick-up and drop-off time, use the format dd.mm.yyyy 
        and seperate date and time with a comma\33[;0m
        ''')
        
        date_from = input("\tEnter pick-up date: ")
        date_to = input("\tEnter drop-off date: ")
        # rental_period = start_date + " - " + end_date
        
        #print ("\t\t\33[;36mRental period: \33[;0m", rental_period) 
        contract_made = input ("\tDate of booking: ")
        country = input("\tCountry of rental: ")
>>>>>>> 740112713ca5ca12bd06adc2adafc33235548c7e

                keys = list(updates.keys())

                if(len(keys) > 0):
                        col = keys[0]
                        self.success_msg = "{} has been modified".format(col.capitalize())


                def print_contract():
                        pass

    # Prints out table of employee
        def print_contracts(self, contract, start, end, current_page, last_page):
                print("|{:^6}|{:^15}|{:^30}|{:^40}|{:^30}|{:^20}|{:^20}|{:^30}|{:^15}|".format("ID", "Role", "Name", "Email", "Social security number", "Mobile phone", "Home phone", "Address", "Postal code"))
                print('-' * 216)
                for i in range(start, end):
                        print("|{:^6}|{:<15}|{:<30}|{:<40}|{:<30}|{:<20}|{:<20}|{:<30}|{:<15}|".format(employees[i].id, employees[i].role, employees[i].name, employees[i].email, employees[i].ssn, employees[i].phone, employees[i].homephone, employees[i].address, employees[i].postal))
                print("{:^216}".format("Page {} of {}".format(current_page, last_page)))
                self.printer.new_line()
        
