from logic.MainLogic import MainLogic
from models.Vehicle import Vehicle
from models.VehicleType import VehicleType

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

        self.menu()


    def create(self):
        counter = 0

        manufacturer = ""
        model = ""
        vehicle_type_id = ""
        status = ""
        man_year = ""
        color = ""
        licence_type = ""
        location_id = ""
        id = ""
        
        vehicle_id_page = 1
        role_page = 1
        while True:

            vehicle = self.logic.get_vehicle_by_id(id)
            if vehicle is None:
                vehicle = ""

            self.printer.header("Create vehicle")
            print(f"ID:\t\t\t\t{id}\nManufacturer:\t\t\t{manufacturer}\nModel:\t\t\t\t{model}\nVehicle Type:\t\t\t{vehicle_type_id}\nStatus:\t\t\t\t{status}\nManufacturing Year:\t\t{man_year}\nColor:\t\t\t\t{color}\nLicence Type:\t\t\t{licence_type}\nLocation:\t\t\t{location_id}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.notification()
            next_input = True
            data = None
            try:
                if counter == 0:
                    data = self.input.get_input("manufacturer",["required"], warning_msg = self.warning_msg)
                    response = data[0]               
                    if response:
                        manufacturer = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                        """role_page = data[2]"""
                elif counter == 1:
                    data = self.input.get_input("model", ["required"], warning_msg = self.warning_msg)
                    response = data[0]    
                    if data[0]:
                        model = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 2:
                    data = self.input.get_input("vehicle_type_id", ["required", "vehicle_type_id"], warning_msg = self.warning_msg)
                    if data[0]:
                        vehicle_type_id = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 3:
                    data = self.input.get_input("status", ["required", "status"], warning_msg = self.warning_msg)
                    if data[0]:
                        status = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 4:
                    data = self.input.get_input("man_year", ["required", "man_year"], warning_msg = self.warning_msg)
                    if data[0]:
                        man_year = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 5:
                    data = self.input.get_input("Color", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        color = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 6:
                    data = self.input.get_input("licence_type", ["required", "licence_type"], warning_msg = self.warning_msg)
                    if data[0]:
                        licence_type = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 7:
                    data = self.input.get_input("location_id", ["required", "location_id"], warning_msg = self.warning_msg)
                    if data[0]:
                        location_id = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 8:
                    vehicles = self.logic.get_all_vehicles()
                    available_vehicles = [[vehicle.id, vehicle] for vehicle in vehicles]
                    vehicle_input = self.input.get_option("vehicle", available_vehicles, current_page = vehicle_id_page, warning_msg = self.warning_msg)
                    if vehicle_input[0] == True:
                        vehicle_id = vehicle_input[1]
                    else:
                        next_input = False
                        self.warning_msg = vehicle_input[1]
                        vehicle_id_page = vehicle_input[2]
                elif counter > 8:
                    new_vehicle = Vehicle(manufacturer, model, vehicle_type_id, status, man_year, color, licence_type, location_id)
                    confirmation = input("Are you sure you want to create this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_vehicle(new_vehicle)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break

    def create_type(self):
        counter = 0

        name = ""
        location_id = ""
        rate = ""
        id = ""
        
        vehicle_id_page = 1
        role_page = 1
        while True:

            vehicle = self.logic.get_vehicle_by_id(id)
            if vehicle is None:
                vehicle = ""

            self.printer.header("Create vehicle type")
            print(f"ID:\t\t\t\t{id}\nName:\t\t\t{name}\nLocation:\t\t{location_id}\nRate:\t\t\t{rate}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.notification()
            next_input = True
            data = None
            try:
                if counter == 0:
                    data = self.input.get_input("name",["required"], warning_msg = self.warning_msg)
                    response = data[0]               
                    if response:
                        name = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                        """role_page = data[2]"""
                elif counter == 1:
                    data = self.input.get_input("location_id", ["required"], warning_msg = self.warning_msg)
                    response = data[0]    
                    if data[0]:
                        location_id = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 2:
                    data = self.input.get_input("rate", ["required", "rate"], warning_msg = self.warning_msg)
                    if data[0]:
                        rate = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter > 2:
                    new_vehicletype = VehicleType(name,location_id,rate)
                    confirmation = input("Are you sure you want to create this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_vehicletype(new_vehicletype)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break

    # Prints out vehicle's menu
    def menu(self):
        while True:
            self.printer.header("Vehicles Menu")
            self.printer.print_options(['Create an vehicle', 'View vehicles', 'Create Vehicle Type', 'View vehicle type'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

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
            self.print(vehicles, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()

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
                vehicle_id = input("Select vehicle by ID: ").lower()
                if vehicle_id == 'q':
                    break
                vehicle = self.logic.get_vehicle_by_id(vehicle_id)
                if vehicle is None:
                    self.warning_msg = "Vehicle not found"
                else:
                    self.vehicle(vehicle_id)
            else:
                self.warning_msg = "Please select available option"

    def view_by_type(self, created = False):
        current_page = 1
        while True:   
            vehicle_type = self.logic.get_all_vehicletypes()
            vehicles_count = len(vehicle_type)
            last_page = int(vehicles_count / self.items_per_page) + (vehicles_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else vehicles_count

            self.printer.header("View vehicle type")
            self.print_type(vehicle_type, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("(N)ext page / (P)revious page / (S)elect vehicle type: ").lower()

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
                vehicle_id = input("Select vehicle type by ID: ").lower()
                if vehicle_id == 'q':
                    break
                vehicle = self.logic.get_vehicletype_by_id(vehicle_id)
                if vehicle is None:
                    self.warning_msg = "Vehicle not found"
                else:
                    self.vehicle_type(vehicle_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single vehicle
    def vehicle(self, vehicle_id):
        while True:
            vehicle = self.logic.get_vehicle_by_id(vehicle_id)
            self.printer.header("View vehicle")
            print("ID:\t\t\t\t{}\nManufacturer:\t\t\t{}\nModel:\t\t\t\t{}\nVehicle Type:\t\t\t{}\nStatus:\t\t\t\t{}\nManufacturing Year:\t\t{}\nColor:\t\t\t\t{}\nLicence Type:\t\t\t{}\nLocation:\t\t\t{}\nVehicle:\t\t\t{}\n".format(vehicle.id, vehicle.manufacturer, vehicle.model, vehicle.vehicle_type_id, vehicle.status, vehicle.man_year, vehicle.color, vehicle.licence_type, vehicle.location_id, self.logic.get_vehicle_by_id(vehicle.id)))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(vehicle.id)
            elif action == 'd' or action == 'delete':
                if self.delete(vehicle.id):
                    self.success_msg = "Vehicle has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"

    def vehicle_type(self, vehicle_id):
        while True:
            vehicle = self.logic.get_vehicletype_by_id(vehicle_id)
            self.printer.header("View vehicle type")
            print("ID:\t\t\t{}\nName:\t\t\t{}\nLocation:\t\t{}\nRate:\t\t\t{}\n".format(vehicle.id, vehicle.name, vehicle.location_id, vehicle.rate))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit_type(vehicle.id)
            elif action == 'd' or action == 'delete':
                if self.delete_type(vehicle.id):
                    self.success_msg = "Vehicle has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"
    
    # Prints out table of vehicle
    def print(self, vehicles, start, end, current_page, last_page):
        if len(vehicles) > 0:
            print("|{:^6}|{:^15}|{:^19}|{:^20}|{:^20}|{:^20}|{:^20}|{:^25}|{:^15}|{:^15}|".format("ID", "Manufacturer", "Model", "Vehicle Type", "Status", "Manufacturing Year", "Color", "Licence Type", "Location", "Vehicle"))
            print('-' * 186)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<19}|{:<20}|{:<20}|{:<20}|{:<20}|{:<25}|{:<15}|{:<15}|".format(vehicles[i].id, vehicles[i].manufacturer, vehicles[i].model, vehicles[i].vehicle_type_id, vehicles[i].status, vehicles[i].man_year, vehicles[i].color, vehicles[i].licence_type, vehicles[i].location_id, self.logic.get_vehicle_by_id(vehicles[i].id).__str__()))
            print("{:^186}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No vehicles found"

    def print_type(self, vehicle_type, start, end, current_page, last_page):
        if len(vehicle_type) > 0:
            print("|{:^6}|{:^15}|{:^19}|{:^20}|".format("ID", "Name", "Location", "Rate"))
            print('-' * 65)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<19}|{:<20}|".format(vehicle_type[i].id, vehicle_type[i].name, vehicle_type[i].location_id, vehicle_type[i].rate, self.logic.get_vehicle_by_id(vehicle_type[i].id).__str__()))
            print("{:^65}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No vehicles found"
  

    def edit(self, vehicle_id):
        vehicle_id_page = 1
        role_page = 1
        while True:
            vehicle = self.logic.get_vehicle_by_id(vehicle_id)
            update = {}
            self.printer.header("Edit vehicle")
            print(f"ID:\t\t\t\t{vehicle.id}\nManufacturer:\t\t\t{vehicle.manufacturer}\nModel:\t\t\t\t{vehicle.model}\nVehicle Type:\t\t\t{vehicle.vehicle_type_id}\nStatus:\t\t\t\t{vehicle.status}\nManufacturing Year:\t\t{vehicle.man_year}\nColor:\t\t\t\t{vehicle.color}\nLicence Type:\t\t\t{vehicle.licence_type}\nLocation:\t\t\t{vehicle.location_id}\nVehicle:\t\t\t{self.logic.get_vehicle_by_id(vehicle.id)}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit Manufacturer', 'Edit Model', 'Edit Vehicle Type', 'Edit Status', 'Edit Manufacturing Year', 'Edit Color', 'Edit Licence', 'Edit Location'])
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
                            data = self.input.get_input("manufacturer", ["required"], current_page = role_page, warning_msg = self.warning_msg)
                            if data[0]:
                                update["manufacturer"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                role_page = data[2]
                                
                    elif action == "2":
                        while True:
                            data = self.input.get_input("model", ["required", "model"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["model"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "3":
                        while True:
                            data = self.input.get_input("vehicle_type_id", ["required", "vehicle_type_id"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["vehicle_type_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "4":
                        while True:
                            data = self.input.get_input("status", ["required", "status"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["status"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "5":
                        while True:
                            data = self.input.get_input("man_year", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["man_year"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "6":
                        while True:
                            data = self.input.get_input("color", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["color"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "7":
                        while True:
                            data = self.input.get_input("licence_type", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["licence_type"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "8":
                        while True:
                            data = self.input.get_input("location_id", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["location_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "9":
                        while True:
                            vehicles = self.logic.get_all_vehicles()
                            available_vehicles = [[vehicle.id, vehicle] for vehicle in vehicles]
                            data = self.input.get_option("vehicle", available_vehicles, current_page = vehicle_id_page, warning_msg = self.warning_msg)
                            if data[0] == True:
                                update["vehicle_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                vehicle_id_page = data[2]
                    if(len(update) > 0):
                        self.logic.update_vehicle(vehicle_id, update)
                        self.success_msg = "Vehicle has been modified"
                except ValueError:
                    break

    def edit_type(self, vehicle_id):
        while True:
            vehicle = self.logic.get_vehicletype_by_id(vehicle_id)
            update = {}
            self.printer.header("Edit vehicle type")
            print(f"ID:\t\t\t{vehicle.id}\nName:\t\t\t{vehicle.name}\nLocation:\t\t{vehicle.location_id}\nRate:\t\t\t{vehicle.rate}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit Name', 'Edit Location', 'Edit Rate'])
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
                            data = self.input.get_input("name", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["name"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                role_page = data[2]
                                
                    elif action == "2":
                        while True:
                            data = self.input.get_input("location_id", ["required", "location_id"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["location_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "3":
                        while True:
                            data = self.input.get_input("rate", ["required", "rate"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["rate"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    if(len(update) > 0):
                        self.logic.update_vehicletype(vehicle_id, update)
                        self.success_msg = "Vehicle has been modified"
                except ValueError:
                    break

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
    def notification(self):
        if not self.warning_msg == "":
            self.printer.print_warning(self.warning_msg)
            self.warning_msg = ""
        elif not self.success_msg == "":
            self.printer.print_success(self.success_msg)
            self.success_msg = ""
        else:
            self.printer.new_line()