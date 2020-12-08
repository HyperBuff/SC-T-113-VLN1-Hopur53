from logic.MainLogic import MainLogic
from models.Location import Location

from ui.PrinterUI import PrinterUI
from ui.InputUI import InputUI

class LocationUI:

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
        location_id = ""
        
        location_id_page = 1
        role_page = 1
        while True:

            location = self.logic.get_location_by_id(location_id)
            if location is None:
                location = ""

            self.printer.header("Create location")
            print(f"Role:\t\t\t\t{role}\nName:\t\t\t\t{name}\nEmail:\t\t\t\t{email}\nSocial security number:\t\t{ssn}\nMobile phone:\t\t\t{phone}\nHome phone:\t\t\t{homephone}\nAddress:\t\t\t{address}\nPostal code:\t\t\t{postal}\nLocation:\t\t\t{location}\n")
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
                    new_location = Location(role, name, address, postal, ssn, phone, homephone, email, location_id)
                    confirmation = input("Are you sure you want to create this location? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_location(new_location)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break

    # Prints out location's menu
    def menu(self):
        while True:
            self.printer.header("locations Menu")
            self.printer.print_options(['Create an location', 'View locations'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("Choose an option: ").lower()
            
            if action == '1':
                if self.create():
                    self.success_msg = "New location has been created"
                    self.view(True)
            elif action == '2':
                self.view()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    # Prints out all location
    def view(self, created = False):
        current_page = 1
        while True:   
            locations = self.logic.get_all_locations()
            locations_count = len(locations)
            last_page = int(locations_count / self.items_per_page) + (locations_count % self.items_per_page > 0)
            if current_page > last_page:
                current_page = last_page
            if created == True:
                current_page = last_page
                created = False
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else locations_count

            self.printer.header("View locations")
            self.print(locations, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()

            action = input("(N)ext page / (P)revious page / (S)elect location: ").lower()

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
                location_id = input("Select location by ID: ").lower()
                if location_id == 'q':
                    break
                location = self.logic.get_location_by_id(location_id)
                if location is None:
                    self.warning_msg = "location not found"
                else:
                    self.location(location_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single location
    def location(self, location_id):
        while True:
            location = self.logic.get_location_by_id(location_id)
            self.printer.header("View location")
            print("ID:\t\t\t\t{}\nRole:\t\t\t\t{}\nName:\t\t\t\t{}\nEmail:\t\t\t\t{}\nSocial security number:\t\t{}\nMobile phone:\t\t\t{}\nHome phone:\t\t\t{}\nAddress:\t\t\t{}\nPostal code:\t\t\t{}\nLocation:\t\t\t{}\n".format(location_id, location.role, location.name, location.email, location.ssn, location.phone, location.homephone, location.address, location.postal, self.logic.get_location_by_id(location.location_id)))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.notification()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(location_id)
            elif action == 'd' or action == 'delete':
                if self.delete(location_id):
                    self.success_msg = "location has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"
    
    # Prints out table of location
    def print(self, locations, start, end, current_page, last_page):
        if len(locations) > 0:
            print("|{:^6}|{:^15}|{:^25}|{:^30}|{:^30}|{:^20}|{:^20}|{:^25}|{:^15}|{:^15}|".format("ID", "Role", "Name", "Email", "Social security number", "Mobile phone", "Home phone", "Address", "Postal code", "Location"))
            print('-' * 212)
            for i in range(start, end):
                print("|{:^6}|{:<15}|{:<25}|{:<30}|{:<30}|{:<20}|{:<20}|{:<25}|{:<15}|{:<15}|".format(locations[i].id, locations[i].role, locations[i].name, locations[i].email, locations[i].ssn, locations[i].phone, locations[i].homephone, locations[i].address, locations[i].postal, self.logic.get_location_by_id(locations[i].location_id).__str__()))
            print("{:^212}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No locations found"
  

    def edit(self, location_id):
        location_id_page = 1
        role_page = 1
        while True:
            location = self.logic.get_location_by_id(location_id)
            update = {}
            self.printer.header("Edit location")
            print(f"ID:\t\t\t\t{location_id}\nRole:\t\t\t\t{location.role}\nName:\t\t\t\t{location.name}\nEmail:\t\t\t\t{location.email}\nSocial security number:\t\t{location.ssn}\nMobile phone:\t\t\t{location.phone}\nHome phone:\t\t\t{location.homephone}\nAddress:\t\t\t{location.address}\nPostal code:\t\t\t{location.postal}\nLocation:\t\t\t{self.logic.get_location_by_id(location.location_id)}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit role', 'Edit email', 'Edit mobile phone', 'Edit home phone', 'Edit address', 'Edit postal code', 'Edit location'])
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
                            locations = self.logic.get_all_locations()
                            available_locations = [[location.id, location] for location in locations]
                            data = self.input.get_option("location", available_locations, current_page = location_id_page, warning_msg = self.warning_msg)
                            if data[0] == True:
                                update["location_id"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                                location_id_page = data[2]
                    if(len(update) > 0):
                        self.logic.update_location(location_id, update)
                        self.success_msg = "location has been modified"
                    break
                except ValueError:
                    break

    # Delete location
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this location? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_location(id)
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