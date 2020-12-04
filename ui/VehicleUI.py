import math

from logic.MainLogic import MainLogic
from models.Vehicle import Vehicle

from ui.PrinterUI import PrinterUI

class VehicleUI:

    def __init__(self):
        self.items_per_page = 10
        self.logic = MainLogic()
        self.printer = PrinterUI()
        self.success_msg = ""
        self.warning_msg = ""

    # Prints out vehicle's menu
    def menu(self):
        while True:
            self.printer.header("Vehicles Menu")
            self.printer.print_options(['Create a vehicle', 'View vehicle'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == '1':
                if self.create():
                    self.success_msg = "New vehicle has been created"
                    self.view()
            elif action == '2':
                self.view()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    # Prints out all vehicles
    def view(self, current_page = 1):

        while True:   
            vehicles = self.logic.get_all_vehicles()
            vehicles_count = len(vehicles)
            last_page = math.ceil(vehicles_count / self.items_per_page)
            self.printer.header("View vehicles")
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else vehicles_count
            self.print_vehicles(vehicles, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(N)ext page / (P)revious page / (S)elect vehicle: ").lower()
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
                vehicle_id = input("Select vehicle by ID: ")
                vehicle = self.logic.get_vehicle_by_id(vehicle_id)
                if vehicle is None:
                    self.warning_msg = "Vehicle not found"
                else:
                    self.select_vehicle(vehicle_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single vehicle
    def select_vehicle(self, vehicle_id):
        while True:
            vehicle = self.logic.get_vehicle_by_id(vehicle_id)
            self.printer.header("View vehicle")
            print("ID:\t\t\t\t{}\nManufacturer:\t\t\t{}\nModel:\t\t\t\t{}\nVehicle type:\t\t\t{}\nManufacturing year:\t\t{}\nColor:\t\t\t\t{}\nLicence type:\t\t\t{}\nLocation:\t\t\t{}\n".format(vehicle_id, vehicle.manufacturer, vehicle.model, vehicle.vehicle_type, vehicle.man_year, vehicle.color, vehicle.licence_type, vehicle.location))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(vehicle_id)
            elif action == 'd' or action == 'delete':
                if self.delete(vehicle_id):
                    self.success_msg = "Vehicle has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"

    # Prints out table of vehicle
    def print_vehicles(self, vehicles, start, end, current_page, last_page):
        print("|{:^6}|{:^20}|{:^15}|{:^25}|{:^10}|{:^25}|{:^20}|{:<20}|{:<20}|".format("ID", "Manufacturer", "Model", "Vehicle type", "Status", "Manufacturing year", "Color", "Licence type", "Location"))
        print('-' * 171)
        for i in range(start, end):
            print("|{:^6}|{:<20}|{:<15}|{:<25}|{:<10}|{:<25}|{:<20}|{:<20}|{:<20}|".format(vehicles[i].id, vehicles[i].manufacturer, vehicles[i].model, vehicles[i].vehicle_type, vehicles[i].status, vehicles[i].man_year, vehicles[i].color, vehicles[i].licence_type, vehicles[i].location))
        print("{:^171}".format("Page {} of {}".format(current_page, last_page)))
        self.printer.new_line()

    # Create vehicle
    def create(self):
        self.printer.header("Add vehicle")
        self.printer.new_line()
        self.printer.print_fail("Press q to go back")
        self.printer.new_line()   
        self.printer.new_line()
        print("Enter vehicle details:")
        while True:
            manufacturer = input("\tEnter manufacturer: ")
            if manufacturer == 'q':
                return
            if len(manufacturer) < 1:
                self.printer.print_warning("Manufacturer must been at least 1 character")
            else:
                break
        while True:
            model = input("\tEnter model: ")
            if model == 'q':
                return
            if len(model) < 1:
                self.printer.print_warning("Model must been at least 1 character")
            #elif not self.logic.is_email_valid(email):
             #   self.printer.print_warning("Email is not valid")
            else:
                break
        while True:
            vehicle_type = input("\tEnter vehicle type: ")
            if vehicle_type == 'q':
                return
            if len(vehicle_type) < 1:
                self.printer.print_warning("Vehicle type must been at least 1 character")
            #elif not self.logic.is_ssn_valid(ssn):
             #   self.printer.print_warning("Social security number is not valid")
            else:
                break

        while True:
            status = input("\tEnter vehicle status: ")
            if status == 'q':
                return
            if len(status) < 1:
                self.printer.print_warning("Vehicle status must been at least 1 character")
            #elif not self.logic.is_ssn_valid(ssn):
             #   self.printer.print_warning("Social security number is not valid")
            else:
                break
        while True:
            man_year = input("\tEnter manufacturing year: ")
            if man_year == 'q':
                return
            if len(man_year) < 1:
                self.printer.print_warning("Manufacturing year must been at least 1 character")
            #elif not self.logic.is_phone_number_valid(phone):
             #   self.printer.print_warning("Phone number is not valid")
            else:
                break
        while True:
            color = input("\tEnter color: ")
            if color == 'q':
                return
            if len(color) < 1:
                self.printer.print_warning("Color must been at least 1 character")
            #elif not self.logic.is_phone_number_valid(phone):
             #   self.printer.print_warning("Phone number is not valid")
            else:
                break
        while True:
            license_type = input("\tEnter licence type: ")
            if license_type == 'q':
                return
            if len(license_type) < 1:
                self.printer.print_warning("Licence type must been at least 1 character")
            else:
                break
        while True:
            location = input("\tEnter location: ")
            if location == 'q':
                return
            if len(location) < 1:
                self.printer.print_warning("Location must been at least 1 character")
            else:
                break
        new_vehicle = Vehicle(manufacturer, model, vehicle_type, status, man_year, color, license_type, location)
        self.logic.create_vehicle(new_vehicle)
        return True
    # Edit vehicle
    def edit(self, id):
        while True:
            updates = {}
            self.printer.header("Edit vehicle")
            self.printer.print_options(['Change manufacturer', 'Change model', 'Change vehicle type', 'Change manufacturing year', 'Change color', 'Change licence type','Change location'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == 'q':
                break

            if action == '1':
                while True:
                    manufacturer = input("\tEnter manufacturer: ")
                    if manufacturer == 'q':
                        break
                    if len(manufacturer) < 1:
                        self.printer.print_warning("Manufacturer must been at least 1 character")
                    #elif not self.logic.is_email_valid(email):
                     #   self.printer.print_warning("Email is not valid")
                    else:
                        updates["manufacturer"] = manufacturer
                        break
            elif action == '2':
                while True:
                    model = input("\tEnter model: ")
                    if model == 'q':
                        break
                    if len(model) < 1:
                        self.printer.print_warning("Model must been at least 1 character")
                    #elif not self.logic.is_phone_number_valid(phone):
                     #   self.printer.print_warning("Phone number is not valid")
                    else:
                        updates["model"] = model
                        break
            elif action == '3':
                while True:
                    vehicle_type = input("\tEnter vehicle type: ")
                    if vehicle_type == 'q':
                        break
                    if len(vehicle_type) < 1:
                        self.printer.print_warning("Vehicle type must been at least 1 character")
                    #elif not self.logic.is_phone_number_valid():
                     #   self.printer.print_warning("Phone number is not valid")
                    else:
                        updates["vehicle type"] = vehicle_type
                        break
            elif action == '4':
                while True:
                    man_year = input("\tEnter manufacturing year: ")
                    if man_year == 'q':
                        break
                    #if len(man_year) < 1:
                     #   self.printer.print_warning("Manu must been at least 1 character")
                    #else:
                     #   updates["address"] = address
                      #  break
            elif action == '5':
                while True:
                    color = input("\tEnter color: ")
                    if color == 'q':
                        return
                    if len(color) < 1:
                        self.printer.print_warning("Color must been at least 1 character")
                    else:
                        updates["color"] = color
                        break
            
            elif action == '6':
                while True:
                    license_type = input("\tEnter licence type: ")
                    if color == 'q':
                        return
                    if len(license_type) < 1:
                        self.printer.print_warning("Licence type must been at least 1 character")
                    else:
                        updates["licence type"] = license_type
                        break
            
            elif action == '7':
                while True:
                    location = input("\tEnter location: ")
                    if location == 'q':
                        return
                    if len(location) < 1:
                        self.printer.print_warning("Location must been at least 1 character")
                    else:
                        updates["location"] = location
                        break
            self.logic.update_vehicle(id, updates)

            keys = list(updates.keys())

            if(len(keys) > 0):
                col = keys[0]
                self.success_msg = "{} has been modified".format(col.capitalize())


    # Delete vehicle
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_vehicle(id)
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

   
