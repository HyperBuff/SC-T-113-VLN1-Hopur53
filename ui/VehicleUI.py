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

        self.menu()


    def create(self):
        counter = 0

        role = ""
        name = ""
        email = ""
        ssn = ""
        phone = ""
        homephone = ""
        address = ""
        postal = ""
        vehicle_id = ""
        
        vehicle_id_page = 1
        role_page = 1
        while True:

            vehicle = self.logic.get_vehicle_by_id(vehicle_id)
            if vehicle is None:
                vehicle = ""

            self.printer.header("Create vehicle")
            print(f"Role:\t\t\t\t{role}\nName:\t\t\t\t{name}\nEmail:\t\t\t\t{email}\nSocial security number:\t\t{ssn}\nMobile phone:\t\t\t{phone}\nHome phone:\t\t\t{homephone}\nAddress:\t\t\t{address}\nPostal code:\t\t\t{postal}\nvehicle:\t\t\t{vehicle}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.notification()
            next_input = True
            data = None
            try:
                if counter == 0:
                    data = self.input.get_option("role", ["Admin", "Delivery", "Booking", "Mechanic", "Financial"], current_page = role_page, warning_msg = self.warning_msg)
                    response = data[0]               
                    if response:
                        role = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                        role_page = data[2]
                elif counter == 1:
                    data = self.input.get_input("name", ["required"], warning_msg = self.warning_msg)
                    response = data[0]    
                    if data[0]:
                        name = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 2:
                    data = self.input.get_input("email", ["required", "email"], warning_msg = self.warning_msg)
                    if data[0]:
                        email = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 3:
                    data = self.input.get_input("social security number", ["required", "ssn"], warning_msg = self.warning_msg)
                    if data[0]:
                        ssn = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 4:
                    data = self.input.get_input("mobile phone", ["required", "phone"], warning_msg = self.warning_msg)
                    if data[0]:
                        phone = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 5:
                    data = self.input.get_input("home phone", ["required", "phone"], warning_msg = self.warning_msg)
                    if data[0]:
                        homephone = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 6:
                    data = self.input.get_input("address", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        address = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 7:
                    data = self.input.get_input("postal code", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        postal = data[1]
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
                    new_vehicle = vehicle(role, name, address, postal, ssn, phone, homephone, email, vehicle_id)
                    confirmation = input("Are you sure you want to create this vehicle? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_vehicle(new_vehicle)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break

    # Prints out vehicle's menu
    def menu(self):
        while True:
            self.printer.header("vehicles Menu")
            self.printer.print_options(['Create an vehicle', 'View vehicles'])
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
                vehicle_id = input("Select vehicle by ID: ")
                vehicle = self.logic.get_vehicle_by_id(vehicle_id)
                if vehicle is None:
                    self.warning_msg = "vehicle not found"
                else:
                    self.vehicle(vehicle_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single vehicle
    def vehicle(self, vehicle_id):
        while True:
            vehicle = self.logic.get_vehicle_by_id(vehicle_id)
            self.printer.header("View vehicle")
            print("ID:\t\t\t\t{}\nRole:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\nvehicle:\t\t\t{}\n".format(vehicle_id, vehicle.role, vehicle.name, vehicle.email, vehicle.ssn, vehicle.phone, vehicle.homephone, vehicle.address, vehicle.postal, self.logic.get_vehicle_by_id(vehicle.vehicle_id)))
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
    
    # Prints out table of vehicle
    def print(self, vehicles, start, end, current_page, last_page):
        if len(vehicles) > 0:
            print("|{:^6}|{:^15}|{:^25}|{:^30}|{:^30}|{:^20}|{:^20}|{:^25}|{:^15}|{:^15}|".format("ID", "Role", "Name", "Email", "Social security number", "Mobile phone", "Home phone", "Address", "Postal code", "vehicle"))
            print('-' * 212)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<25}|{:<30}|{:<30}|{:<20}|{:<20}|{:<25}|{:<15}|{:<15}|".format(vehicles[i].id, vehicles[i].role, vehicles[i].name, vehicles[i].email, vehicles[i].ssn, vehicles[i].phone, vehicles[i].homephone, vehicles[i].address, vehicles[i].postal, self.logic.get_vehicle_by_id(vehicles[i].vehicle_id).__str__()))
            print("{:^212}".format("Page {} of {}".format(current_page, last_page)))
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
            print(f"ID:\t\t\t\t{vehicle_id}\nRole:\t\t\t\t{vehicle.role}\nName:\t\t\t\t{vehicle.name}\nEmail:\t\t\t\t{vehicle.email}\nSocial security number:\t\t{vehicle.ssn}\nMobile phone:\t\t\t{vehicle.phone}\nHome phone:\t\t\t{vehicle.homephone}\nAddress:\t\t\t{vehicle.address}\nPostal code:\t\t\t{vehicle.postal}\nvehicle:\t\t\t{self.logic.get_vehicle_by_id(vehicle.vehicle_id)}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit role', 'Edit email', 'Edit mobile phone', 'Edit home phone', 'Edit address', 'Edit postal code', 'Edit vehicle'])
            self.printer.new_line()
            self.notification()
            while True:
                action = input("Choose an option: ").lower()
                data = None
                try:
                    if action == "q":
                        break
                    elif action == "1":
                        while True:
                            data = self.input.get_option("role", ["Admin", "Delivery", "Booking", "Mechanic", "Financial"], current_page = role_page, warning_msg = self.warning_msg)
                            if data[0]:
                                update["role"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                role_page = data[2]
                                
                    elif action == "2":
                        while True:
                            data = self.input.get_input("email", ["required", "email"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["email"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "3":
                        while True:
                            data = self.input.get_input("mobile phone", ["required", "phone"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["phone"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "4":
                        while True:
                            data = self.input.get_input("home phone", ["required", "phone"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["homephone"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "5":
                        while True:
                            data = self.input.get_input("address", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["address"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "6":
                        while True:
                            data = self.input.get_input("postal code", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["postal"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "7":
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
                        self.success_msg = "vehicle has been modified"
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