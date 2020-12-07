from models.VehicleType import VehicleType
from logic.MainLogic import MainLogic
from models.Vehicle import Vehicle

from ui.PrinterUI import PrinterUI
from ui.InputUI import InputUI

class VehicleUI:

    def __init__(self):
        self.items_per_page = 10

        self.logic = MainLogic()
        self.printer = PrinterUI()
        self.input = InputUI()

        self.success_msg = ""
        self.warning_msg = ""

    # Prints out vehicle's menu
    def menu(self):
        while True:
            self.printer.header("Vehicles Menu")
            self.printer.print_options(['Create a vehicle', 'View vehicles', 'Create a vehicle type', 'View vehicle types'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                if self.create():
                    self.success_msg = "New vehicle has been created"
                    self.view(True)
            elif action == '2':
                self.view()
            elif action == '3':
                if self.create_type():
                    self.success_msg = "New vehicle type has been created"
                    self.view_by_type(True)
            elif action == '4':
                self.view_by_type()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    # Prints out all vehicle
    def view(self, created = False):
        current_page = 1
        while True:   
            vehicles = self.logic.get_all_vehicles()
            vehicles_count = len(vehicles)
            last_page = int(vehicles_count / self.items_per_page) + (vehicles_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else vehicles_count

            self.printer.header("View vehicles")
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

    def view_by_type(self, created = False, return_id = False):
        current_page = 1
        while True:   
            vehicle_types = self.logic.get_all_vehicletypes()
            vehicles_count = len(vehicle_types)
            last_page = int(vehicles_count / self.items_per_page) + (vehicles_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else vehicles_count

            self.printer.header("View vehicle types")
            self.print_vehicle_types(vehicle_types, start, end, current_page, last_page)
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
                vehicletype_id = input("Select vehicle by ID: ")
                vehicle = self.logic.get_vehicletype_by_id(vehicletype_id)
                if vehicle is None:
                    self.warning_msg = "Vehicle not found"
                else:
                    if return_id:
                        return vehicletype_id
                    else:
                        self.select_vehicle_by_type(vehicletype_id)
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
    
    def select_vehicle_by_type(self, vehicletype_id):
        while True:
            vehicle_type = self.logic.get_vehicletype_by_id(vehicletype_id)
            self.printer.header("View vehicle type")
            print("ID:\t\t\t{}\nName:\t\t\t{}\nRegions:\t\t{}\nRate:\t\t\t{}\n".format(vehicle_type.id, vehicle_type.name, vehicle_type.regions, vehicle_type.rate))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit_type(vehicletype_id)
            elif action == 'd' or action == 'delete':
                if self.delete_type(vehicletype_id):
                        self.success_msg = "Vehicle has been deleted"
                        break
            else:
                self.warning_msg = "Please select available option"

            
    # Prints out table of vehicle
    def print_vehicles(self, vehicles, start, end, current_page, last_page):
        if len(vehicles) > 0:
            print("|{:^6}|{:^20}|{:^15}|{:^25}|{:^10}|{:^25}|{:^20}|{:<20}|{:<20}|".format("ID", "Manufacturer", "Model", "Vehicle type", "Status", "Manufacturing year", "Color", "Licence type", "Location"))
            print('-' * 171)
            for i in range(start, end):
                print("|{:^6}|{:<20}|{:<15}|{:<25}|{:<10}|{:<25}|{:<20}|{:<20}|{:<20}|".format(vehicles[i].id, vehicles[i].manufacturer, vehicles[i].model, vehicles[i].vehicle_type, vehicles[i].status, vehicles[i].man_year, vehicles[i].color, vehicles[i].licence_type, vehicles[i].location))
            print("{:^171}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No vehicles found"

    def print_vehicle_types(self, vehicle_type, start, end, current_page, last_page):
        if len(vehicle_type) > 0:
            print("|{:^6}|{:^20}|{:^15}|{:^25}|".format("ID", "Name", "Regions", "Rate"))
            print('-' * 71)
            for i in range(start, end):
                print("|{:^6}|{:<20}|{:<15}|{:<25}|".format(vehicle_type[i].id, vehicle_type[i].name, vehicle_type[i].regions, vehicle_type[i].rate))
            print("{:^71}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No vehicle types found"

    # Create vehicle
    def create(self):
        self.printer.header("Add vehicle")
        self.printer.new_line()
        self.printer.print_fail("Press q to go back")
        self.printer.new_line()
        try:
            manufacturer = self.input.get_input("manufacturer")
            model = self.input.get_input("model")
            vehicle_type = self.view_by_type(return_id=True)
            status = self.input.get_input("status")
            man_year = self.input.get_input("manufacturing year", ["year"])
            color = self.input.get_input("color")
            licence_type = self.input.get_input("licence type")
            location = self.input.get_input("location")
            new_vehicle = Vehicle(manufacturer, model, vehicle_type, status, man_year, color, licence_type, location)
            self.logic.create_vehicle(new_vehicle)
            return True
        except ValueError:
            return False
    
    def create_type(self):
        self.printer.header("Add vehicle type")
        self.printer.new_line()
        self.printer.print_fail("Press q to go back")
        self.printer.new_line()
        try:
            name = self.input.get_input("name")
            regions = self.input.get_input("regions")
            rate = self.input.get_input("rate")
            vehicle = VehicleType(name, regions, rate)
            self.logic.create_vehicletype(vehicle)
            return True
        except ValueError:
            return False

    # Edit vehicle
    def edit(self, id):
        while True:
            updates = {}
            self.printer.header("Edit vehicle")
            self.printer.print_options(['Change manufacturer', 'Change model', 'Change vehicle type', 'Change status','Change manufacturing year', 'Change color', 'Change licence type','Change location'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == 'q':
                break
            elif action == '1':
                try:
                    manufacturer = self.input.get_input("manufacturer")
                    updates["manufacturer"] = manufacturer
                except ValueError:
                    break
            elif action == '2':
                try:
                    model = self.input.get_input("model")
                    updates["model"] = model
                except ValueError:
                    break
            elif action == '3':
                try:
                    vehicle_type = self.input.get_input("vehicle type")
                    updates["vehicle_type"] = vehicle_type
                except ValueError:
                    break
            elif action == '5':
                try:
                    status = self.input.get_input("status")
                    updates["status"] = status
                except ValueError:
                    break
            elif action == '5':
                try:
                    man_year = self.input.get_input("manufacturing year", ["year"])
                    updates["man_year"] = man_year
                except ValueError:
                    break
            elif action == '6':
                try:
                    color = self.input.get_input("color")
                    updates["color"] = color
                except ValueError:
                    break
            elif action == '7':
                try:
                    licence_type = self.input.get_input("licence type")
                    updates["licence_type"] = licence_type
                except ValueError:
                    break
            elif action == '8':
                try:
                    location = self.input.get_input("location")
                    updates["location"] = location
                except ValueError:
                    break
            else:
                self.warning_msg = "Please select available option"

            if(len(updates) > 0):
                self.logic.update_vehicle(id, updates)
                self.success_msg = "{} has been modified".format(list(updates.keys())[0].capitalize())

    def edit_type(self, id):
        while True:
            updates = {}
            self.printer.header("Edit vehicle type")
            self.printer.print_options(['Change name', 'Change regions', 'Change vehicle rate'])
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
                    regions = self.input.get_input("regions")
                    updates["regions"] = regions
                except ValueError:
                    break
            elif action == '3':
                try:
                    rate = self.input.get_input("rate")
                    updates["rate"] = rate
                except ValueError:
                    break
            else:
                self.warning_msg = "Please select available option"

            if(len(updates) > 0):
                self.logic.update_vehicletype(id, updates)
                self.success_msg = "{} has been modified".format(list(updates.keys())[0].capitalize())

    # Delete vehicle
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_vehicle(id)
            return True
        return False

    def delete_type(self, id):  
        confirmation = input("Are you sure you want to delete this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_vehicletype(id)
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
