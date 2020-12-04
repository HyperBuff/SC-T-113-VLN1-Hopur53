import math

from logic.MainLogic import MainLogic
from models.Location import Location

from ui.PrinterUI import PrinterUI


class LocationUI:

    def __init__(self):
        self.logic = MainLogic()
        self.printer = PrinterUI()
        self.items_per_page = 10
        self.success_msg = ""
        self.warning_msg = ""
    

    def menu(self):
        while True:
            self.printer.header("Location Menu")
            self.printer.print_options(['Create new location', 'Modify location information', 'View location information', 'View opening hour overview'])
            self.printer.new_line(2)
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("Choose an option: ").lower()
            if action == '1':
                if self.create():
                    self.success_msg = "New location has been created"
                    self.view()
            elif action == '2':
                self.edit(id)
            elif action == '3':
                self.view()
            elif action == '4':
                self.opening_hours()
            elif action == 'q':
                break
            else:
                self.warning_msg = "Please select available option"

    
    # Prints out all locations
    def view(self, current_page = 1):

        while True:   
            locations = self.logic.get_all_locations()
            locations_count = len(locations)
            last_page = math.ceil(locations_count / self.items_per_page)
            self.printer.header("View locations")
            start = (current_page - 1) * self.items_per_page
            end = start + 10 if not current_page == last_page else locations_count
            self.print_locations(locations, start, end, current_page, last_page)
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(N)ext page / (P)revious page / (S)elect employee: ").lower()
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
                    self.warning_msg = "Location not found"
                else:
                    self.select_location(location_id)
            else:
                self.warning_msg = "Please select available option"


    # Prints out single location
    def select_location(self, location_id):
        while True:
            location = self.logic.get_location_by_id(location_id)
            self.printer.header("View location")
            print("Country:\t\t\t\t{}\nAirport:\t\t\t\t{}\nPhone number:\t\t\t\t{}\nOpening hours:\t\t\t\t{}ID:\t\t\t\t{}\n".format(location.country, location.airport, location.phone, location.opening_hours, location_id))
            self.printer.new_line()
            self.printer.print_fail("Press q to go back")
            self.print_msg()
            action = input("(E)dit / (D)elete: ").lower()
            if action == 'q':
                break
            elif action == 'e' or action == 'edit':
                self.edit(location_id)
            elif action == 'd' or action == 'delete':
                self.delete(location_id)
                self.success_msg = "Location has been deleted"
                break
            else:
                self.warning_msg = "Please select available option"
            

    # Prints out table of locations
    def print_locations(self, location, start, end, current_page, last_page):
        print("|{:^40}|{:<30}|{:<35}|{:<20}|{:<20}|".format("ID", "Country", "Airport", "Phone number", "Opening hours"))
        print('-' * 216)
        for i in range(start, end):
            print("|{:^40}|{:<30}|{:<35}|{:<20}|{:<20}|".format(location[i].id, location[i].country, location[i].airport, location[i].phone, location[i].opening_hours))
        print("{:^216}".format("Page {} of {}".format(current_page, last_page)))
        self.printer.new_line()


    # Create location
    def create(self):
        self.printer.header("Add location")
        self.printer.new_line()
        self.printer.print_fail("Press q to go back")
        self.printer.new_line()
        print("Enter location details:")
        while True:
            country = input("\tEnter country name: ")
            if country == 'q':
                return
            if len(country) < 1:
                self.printer.print_warning("Country name must be at least 1 character")
            else:
                break
        while True:
            airport = input("\tEnter airport: ")
            if airport == 'q':
                return
            if len(airport) < 1:
                self.printer.print_warning("Airport name must be at least 1 character")
            else:
                break
        while True:
            phone = input("\tEnter airport's phone number: ")
            if phone == 'q':
                return
            if len(phone) < 1:
                self.printer.print_warning("Phone number must be at least 1 character")
            elif not self.logic.is_phone_number_valid(phone):
                self.printer.print_warning("Phone number is not valid")
            else:
                break
        while True:
            opening_hours = input("\tEnter opening hours: ")
            if opening_hours == 'q':
                return
            if len(opening_hours) < 1:
                self.printer.print_warning("Address must been at least 1 character")
            else:
                break

        new_location = Location(country, airport, phone, opening_hours)
        self.logic.create_location(new_location) 
        return True         
 

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
            if action == '1':
                while True:
                    country = input("\tEnter country: ")
                    if country == 'q':
                        break
                    if len(country) < 1:
                        self.printer.print_warning("Country name must be at least 1 character")
                    else:
                        updates["country"] = country
            elif action == '2':
                while True:
                    airport = input("\tEnter airport: ")
                    if airport == 'q':
                        break
                    if len(airport) < 1:
                        self.printer.print_warning("Airport must be at least 1 character")
                    else:
                        updates["airport"] = airport
                        break
            elif action == '3':
                while True:
                    phone = input("\tEnter airport's phone number: ")
                    if phone == 'q':
                        break
                    if len(phone) < 1:
                        self.printer.print_warning("Phone must be at least 1 character")
                    elif not self.logic.is_phone_number_valid(phone):
                        self.printer.print_warning("Phone number is not valid")
                    else:
                        updates["phone"] = phone
                        break
            elif action == '4':
                while True:
                    opening_hours = input("\tEnter opening hours: ")
                    if phone == 'q':
                        break
                    if len(opening_hours) < 1:
                        self.printer.print_warning("Opening hours must be at least 1 character")
                    else:
                        updates["opening hours"] = opening_hours
                        break
            
            self.logic.update_employee(id, updates)

            keys = list(updates.keys())

            if(len(keys) > 0):
                col = keys[0]
                self.success_msg = "{} has been modified".format(col.capitalize())


    def opening_hours(self):   #Eftir að gera
        pass


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


    


