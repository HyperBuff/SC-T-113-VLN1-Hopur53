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

    # Prints out location's menu
    def menu(self):
        while True:
            self.printer.header("locations Menu")
            self.printer.print_options(['Create an location', 'View locations'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()

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
            self.print_locations(locations, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()

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
                location_id = input("Select location by ID: ")
                location = self.logic.get_location_by_id(location_id)
                if location is None:
                    self.warning_msg = "location not found"
                else:
                    self.select_location(location_id)
            else:
                self.warning_msg = "Please select available option"

    # Prints out single location
    def select_location(self, location_id):
        while True:
            location = self.logic.get_location_by_id(location_id)
            self.printer.header("View location")
            print("ID:\t\t\t\t{}\nCountry:\t\t\t{}\nAirport:\t\t\t{}\nPhone number:\t\t\t{}\nOpening hours:\t\t\t{}\n".format(location_id, location.country, location.airport, location.phone, location.hours))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
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
    def print_locations(self, locations, start, end, current_page, last_page):
        if len(locations) > 0:
            print("|{:^6}|{:<20}|{:<25}|{:<20}|{:<20}|".format("ID", "Country", "Airport", "Phone number", "Opening hours"))
            print('-' * 97)
            for i in range(start, end):
                print("|{:^6}|{:<20}|{:<25}|{:<20}|{:<20}|".format(locations[i].id, locations[i].country, locations[i].airport, locations[i].phone, locations[i].hours))
            print("{:^97}".format("Page {} of {}".format(current_page, last_page)))
            self.printer.new_line()
        else:
            self.warning_msg = "No locations found"

    # Create location
    def create(self):
        self.printer.header("Add location")
        self.printer.new_line()
        self.printer.print_fail("Press q to go back")
        self.printer.new_line()
        try:
            country = self.input.get_input("country")
            airport = self.input.get_input("airport")
            phone = self.input.get_input("phone", ["phone"])
            hours = self.input.get_input("hours")

            new_location = Location(country, airport, phone, hours)
            self.logic.create_location(new_location)
            return True
        except ValueError:
            return False
       
    # Edit location
    def edit(self, id):
        while True:
            updates = {}
            self.printer.header("Edit location")
            self.printer.print_options(['Change country', 'Change airport', 'Change phone', 'Change opening hours'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == 'q':
                break
            elif action == '1':
                try:
                    country = self.input.get_input("country")
                    updates["country"] = country
                except ValueError:
                    break
            elif action == '2':
                try:
                    airport = self.input.get_input("airport")
                    updates["airport"] = airport
                except ValueError:
                    break
            elif action == '3':
                try:
                    phone = self.input.get_input("phone", ["phone"])
                    updates["phone"] = phone
                except ValueError:
                    break
            elif action == '4':
                try:
                    hours = self.input.get_input("hours")
                    updates["hours"] = hours
                except ValueError:
                    break
            else:
                self.warning_msg = "Please select available option"

            if(len(updates) > 0):
                self.logic.update_location(id, updates)
                self.success_msg = "{} has been modified".format(list(updates.keys())[0].capitalize())

    # Delete location
    def delete(self, id):  
        confirmation = input("Are you sure you want to delete this location? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
        if confirmation == 'y':
            self.logic.delete_location(id)
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
