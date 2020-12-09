from logic.MainLogic import MainLogic
from models.Vehicle import Vehicle
from models.VehicleType import VehicleType
from models.Location import Location

from ui.PrinterUI import PrinterUI
from ui.InputUI import InputUI

class VehicleUI:

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
        
        location_id_page = 1
        vehicletype_id_page = 1
        status_page = 1
        while True:

            location = self.logic.get_location_by_id(location_id)
            vehicletype = self.logic.get_vehicletype_by_id(vehicle_type_id)
            if location is None:
                location = ""
            if vehicletype is None:
                vehicletype = ""

            self.printer.header("Create vehicle")
            print(f"Manufacturer:\t\t\t{manufacturer}\nModel:\t\t\t\t{model}\nVehicle type:\t\t\t{vehicletype}\nStatus:\t\t\t\t{status}\nManufacturing year:\t\t{man_year}\nColor:\t\t\t\t{color}\nLicence type:\t\t\t{licence_type}\nLocation:\t\t\t{location}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.notification()
            next_input = True
            data = None
            try:
                if counter == 0:
                    data = self.input.get_input("manufacturer", ["required"], warning_msg = self.warning_msg)
                    response = data[0]               
                    if response:
                        manufacturer = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 1:
                    data = self.input.get_input("model", ["required"], warning_msg = self.warning_msg)
                    response = data[0]    
                    if data[0]:
                        model = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 2:
                    vehicletypes = self.logic.get_all_vehicletypes()
                    available_vehicletypes = [[vehicletype.id, vehicletype] for vehicletype in vehicletypes]
                    data = self.input.get_option("vehicle type", available_vehicletypes, current_page = vehicletype_id_page, warning_msg = self.warning_msg)
                    if data[0] == True:
                        vehicle_type_id = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                        location_id_page = data[2]
                elif counter == 3:
                    data = self.input.get_option("status", ["Available", "Unavailable"], current_page = status_page, warning_msg = self.warning_msg)
                    if data[0]:
                        status = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                        status_page = data[2]
                elif counter == 4:
                    data = self.input.get_input("manufacturing year", ["required", "year"], warning_msg = self.warning_msg)
                    if data[0]:
                        man_year = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 5:
                    data = self.input.get_input("color", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        color = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 6:
                    data = self.input.get_input("licence type", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        licence_type = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 7:
                    locations = self.logic.get_all_locations()
                    available_locations = [[location.id, location] for location in locations]
                    location_input = self.input.get_option("location", available_locations, current_page = location_id_page, warning_msg = self.warning_msg)
                    if location_input[0] == True:
                        location_id = location_input[1]
                    else:
                        next_input = False
                        self.warning_msg = location_input[1]
                        location_id_page = location_input[2]
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
        
        location_id_page = 1
        while True:

            location = self.logic.get_location_by_id(location_id)
            if location is None:
                location = ""

            self.printer.header("Create vehicle")
            
            print(f"Name:\t\t\t{name}\nLocation:\t\t\t{location}\nRate:\t\t\t\t{rate}\n")
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
                    locations = self.logic.get_all_locations()
                    available_locations = [[location.id, location] for location in locations]
                    location_input = self.input.get_option("location", available_locations, current_page = location_id_page, warning_msg = self.warning_msg)
                    if location_input[0] == True:
                        location_id = location_input[1]
                    else:
                        next_input = False
                        self.warning_msg = location_input[1]
                        location_id_page = location_input[2]
                elif counter == 2:
                    data = self.input.get_input("rate", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        rate = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter > 2:
                    new_vehicle_type = VehicleType(name, location_id, rate)
                    confirmation = input("Are you sure you want to create this vehicle type? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_vehicletype(new_vehicle_type)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break         

    def menu_options(self):
        if self.employee_role.lower() == "admin":
            return {
                "Create a vehicle": self.create,
                "View vehicles": self.view,
                "Create a vehicle type": self.create_type,
                "View vehicles types": self.view_type
            }
        elif self.employee_role.lower() == "mechanic":
            return {
                "Change vehicle status": self.view
            }

    # Prints out vehicle's menu
    def menu(self):
        while True:
            menu_options = self.menu_options()
            self.printer.header("Vehicles Menu")
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

    # Prints out all vehicle
    def view_type(self, created = False):
        current_page = 1
        while True:   
            vehicletypes = self.logic.get_all_vehicletypes()
            vehicletypes_count = len(vehicletypes)
            last_page = int(vehicletypes_count / self.items_per_page) + (vehicletypes_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else vehicletypes_count

            self.printer.header("View vehicles")
            self.print_type(vehicletypes, start, end, current_page, last_page)
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
                vehicletype_id = input("Select vehicle type by ID: ").lower()
                if vehicletype_id == 'q':
                    break
                vehicletype = self.logic.get_vehicletype_by_id(vehicletype_id)
                if vehicletype is None:
                    self.warning_msg = "Vehicle type not found"
                else:
                    self.vehicle_type(vehicletype_id)
            else:
                self.warning_msg = "Please select available option"
   
    # Prints out single vehicle
    def vehicle(self, vehicle_id):
        while True:
            vehicle = self.logic.get_vehicle_by_id(vehicle_id)
            self.printer.header("View vehicle")
            print("ID:\t\t\t\t{}\nManufacturer:\t\t\t{}\nModel:\t\t\t\t{}\nVehicle type:\t\t\t{}\nStatus:\t\t\t\t{}\nManufacturing year:\t\t{}\nColor:\t\t\t\t{}\nLicence type:\t\t\t{}\nLocation:\t\t\t{}\n".format(vehicle.id, vehicle.manufacturer, vehicle.model, self.logic.get_vehicletype_by_id(vehicle.vehicle_type_id), vehicle.status, vehicle.man_year, vehicle.color, vehicle.licence_type, self.logic.get_location_by_id(vehicle.location_id)))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(vehicle_id)
            elif action == 'd' or action == 'delete':
                if self.delete(vehicle_id):
                    self.success_msg = "vehicle has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"
    
    # Prints out single vehicle
    def vehicle_type(self, vehicle_type_id):
        while True:
            vehicletype = self.logic.get_vehicletype_by_id(vehicle_type_id)
            self.printer.header("View vehicle")
            print(f"ID:\t\t\t\t{vehicle_type_id}\nName:\t\t\t{vehicletype.name}\nLocation:\t\t\t{self.logic.get_location_by_id(vehicletype.location_id)}\nRate:\t\t\t\t{vehicletype.rate}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit_type(vehicle_type_id)
            elif action == 'd' or action == 'delete':
                if self.delete_type(vehicle_type_id):
                    self.success_msg = "Vehicle has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"

    # Prints out table of vehicle
    def print(self, vehicles, start, end, current_page, last_page):
        if len(vehicles) > 0:
            print("|{:^6}|{:^15}|{:^19}|{:^20}|{:^20}|{:^20}|{:^20}|{:^25}|{:^15}|".format("ID", "Manufacturer", "Model", "Vehicle type", "Status", "Manufacturing year", "Color", "Licence type", "Location"))
            print('-' * 186)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<19}|{:<20}|{:<20}|{:<20}|{:<20}|{:<25}|{:<15}|".format(vehicles[i].id, vehicles[i].manufacturer, vehicles[i].model, self.logic.get_vehicletype_by_id(vehicles[i].vehicle_type_id).__str__(), vehicles[i].status, vehicles[i].man_year, vehicles[i].color, vehicles[i].licence_type, self.logic.get_location_by_id(vehicles[i].location_id).__str__()))
            print("{:^186}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No vehicles found"
  
    # Prints out table of vehicle
    def print_type(self, vehicletypes, start, end, current_page, last_page):
        if len(vehicletypes) > 0:
            print("|{:^6}|{:^15}|{:^19}|{:^20}|".format("ID", "Name", "Location", "Rate"))
            print('-' * 186)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<19}|{:<20}|".format(vehicletypes[i].id, vehicletypes[i].name, self.logic.get_location_by_id(vehicletypes[i].location_id).__str__(), vehicletypes[i].rate))
            print("{:^186}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No vehicles found"

    def edit(self, vehicle_id):
        vehicletype_id_page = 1
        location_id_page = 1
        while True:
            vehicle = self.logic.get_vehicle_by_id(vehicle_id)
            update = {}
            self.printer.header("Edit vehicle")
            print(f"ID:\t\t\t\t{vehicle_id}\nManufacturer:\t\t\t{vehicle.manufacturer}\nModel:\t\t\t\t{vehicle.model}\nVehicle type:\t\t\t{self.logic.get_vehicletype_by_id(vehicle.vehicle_type_id)}\nStatus:\t\t\t\t{vehicle.status}\nManufacturing year:\t\t{vehicle.man_year}\nColor:\t\t\t\t{vehicle.color}\nLicence type:\t\t\t{vehicle.licence_type}\nLocation:\t\t\t{self.logic.get_location_by_id(vehicle.location_id)}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit manufacturer', 'Edit model', 'Edit vehicle type', 'Edit status', 'Edit manufacturing year', 'Edit color', 'Edit licence', 'Edit location'])
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
                            data = self.input.get_input("manufacturer", ["required"], warning_msg = self.warning_msg)               
                            if data[0]:
                                update["manufacturer"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "2":
                        while True:
                            data = self.input.get_input("model", ["required"], warning_msg = self.warning_msg)               
                            if data[0]:
                                update["model"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "3":
                        while True:
                            vehicletypes = self.logic.get_all_vehicletypes()
                            available_vehicletypes = [[vehicletype.id, vehicletype] for vehicletype in vehicletypes]
                            data = self.input.get_option("vehicle type", available_vehicletypes, current_page = vehicletype_id_page, warning_msg = self.warning_msg)               
                            if data[0]:
                                update["vehicle_type_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                vehicletype_id_page = data[2]
                    elif action == "4":
                        while True:
                            data = self.input.get_option("status", ["Available", "Unavailable"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["status"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "5":
                        while True:
                            data = self.input.get_input("manufacturing year", ["required", "year"], warning_msg = self.warning_msg)
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
                            data = self.input.get_input("licence type", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["licence_type"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "8":
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
                    else:
                        self.warning_msg = "Please select available option"
                    if(len(update) > 0):
                        self.logic.update_vehicle(vehicle_id, update)
                        self.success_msg = "Vehicle has been modified"
                    break
                except ValueError:
                    break
    
    def edit_type(self, vehicle_type_id):
        location_id_page = 1
        while True:
            vehicletype = self.logic.get_vehicletype_by_id(vehicle_type_id)
            update = {}
            self.printer.header("Edit vehicle type")
            print(f"ID:\t\t\t\t{vehicletype.id}\nName:\t\t\t{vehicletype.name}\nLocation:\t\t\t{self.logic.get_location_by_id(vehicletype.location_id)}\nRate:\t\t\t\t{vehicletype.rate}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit name', 'Edit location', 'Edit rate'])
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
                    elif action == "2":
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
                    elif action == "3":
                        while True:
                            data = self.input.get_input("rate", ["required"], warning_msg = self.warning_msg)               
                            if data[0]:
                                update["rate"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    else:
                        self.warning_msg = "Please select available option"
                    if(len(update) > 0):
                        self.logic.update_vehicletype(vehicle_type_id, update)
                        self.success_msg = "Vehicle type has been modified"
                    break
                except ValueError:
                    break

    # Delete vehicle
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_vehicle(id)
            return True
        return False

    # Delete vehicle
    def delete_type(self, id):  
        confirmation = input("Are you sure you want to delete this vehicle type? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
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