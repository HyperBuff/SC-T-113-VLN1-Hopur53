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

        country = ""
        airport = ""
        phone = ""
        hours = ""
        
        while True:

            self.printer.header("Create location")
            print(f"Country:\t\t\t{country}\nAirport:\t\t\t{airport}\nPhone:\t\t\t\t{phone}\nHours:\t\t\t\t{hours}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.notification()
            next_input = True
            data = None
            try:
                if counter == 0:
                    data = self.input.get_input("country", ["required"], warning_msg = self.warning_msg)  
                    if data[0]:
                        country = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 1:
                    data = self.input.get_input("airport", ["required"], warning_msg = self.warning_msg)
                    if data[0]:
                        airport = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 2:
                    data = self.input.get_input("phone", ["required", "phone"], warning_msg = self.warning_msg)
                    if data[0]:
                        phone = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter == 3:
                    data = self.input.get_input("hours", ["required", "hours"], warning_msg = self.warning_msg)
                    if data[0]:
                        hours = data[1]
                    else:
                        next_input = False
                        self.warning_msg = data[1]
                elif counter > 3:
                    new_location = Location(country, airport, phone, hours)
                    confirmation = input("Are you sure you want to create this location? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if confirmation == 'y':
                        self.logic.create_location(new_location)
                        return True
                    return False
                if next_input:
                    counter += 1
            except ValueError:
                break

    def menu(self):
        while True:
            self.printer.header("Locations Menu")
            self.printer.print_options(['Create a location', 'View locations'])
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
                    self.warning_msg = "You are currently on the last page"
                else:
                    current_page += 1
            elif action == 'p' or action == "previous":
                if current_page > 1:
                    current_page -= 1
                else:
                    current_page = 1
                    self.warning_msg = "You are currently on the first page"
            elif action == 's' or action == "select":
                location_id = input("Select location by ID: ").lower()
                if location_id == 'q':
                    break
                location = self.logic.get_location_by_id(location_id)
                if location is None:
                    self.warning_msg = "Location not found"
                else:
                    self.location(location_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single location
    def location(self, location_id):
        while True:
            location = self.logic.get_location_by_id(location_id)
            self.printer.header("View location")
            print("ID:\t\t\t\t{}\nCountry:\t\t\t{}\nAirport:\t\t\t{}\nPhone:\t\t\t\t{}\nOpening hours:\t\t\t{}\n".format(location.id, location.country, location.airport, location.phone, location.hours))
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
                    self.success_msg = "Location has been deleted"
                    break
            else:
                self.warning_msg = "Please select available option"
    
    # Prints out table of location
    def print(self, locations, start, end, current_page, last_page):
        if len(locations) > 0:
            print("|{:^6}|{:^18}|{:^18}|{:^20}|{:^20}|".format("ID", "Country", "Airport", "Phone", "Opening hours"))
            print('-' * 88)
            for i in range(start, end):
                print("|{:^6}|{:<18}|{:<18}|{:<20}|{:<20}|".format(locations[i].id, locations[i].country, locations[i].airport, locations[i].phone, locations[i].hours))
            print("{:^88}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No locations found"
  

    def edit(self, location_id):
        while True:
            location = self.logic.get_location_by_id(location_id)
            update = {}
            self.printer.header("Edit location")
            print(f"ID:\t\t\t\t{location_id}\nCountry:\t\t\t{location.country}\nAirport:\t\t\t{location.airport}\nPhone:\t\t\t\t{location.phone}\nOpening hours:\t\t\t{location.hours}\n")
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.printer.new_line()
            self.printer.print_options(['Edit country', 'Edit airport', 'Edit phone', 'Edit opening hours'])
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
                            data = self.input.get_input("country", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["country"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])                
                    elif action == "2":
                        while True:
                            data = self.input.get_input("airport", ["required"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["airport"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "3":
                        while True:
                            data = self.input.get_input("phone", ["required", "phone"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["phone"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    elif action == "4":
                        while True:
                            data = self.input.get_input("opening hours", ["required", "hours"], warning_msg = self.warning_msg)
                            if data[0]:
                                update["hours"] = data[1]
                                break
                            else:
                                self.printer.print_warning(data[1])
                    else:
                        self.warning_msg = "Please select available option"
                    if(len(update) > 0):
                        self.logic.update_location(location_id, update)
                        self.success_msg = "Location has been modified"
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