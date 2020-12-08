from ui.PrinterUI import PrinterUI

class InputUI:

    def __init__(self):
        self.printer = PrinterUI()
        self.items_per_page = 10

    def get_input(self, title, validations = []):
        while True:
            user_input = input("Enter {}: ".format(title.lower()))
            if user_input == 'q':
                raise ValueError
            elif len(user_input.replace(" ", "")) < 1:
                self.printer.print_warning("{} must been at least 1 character".format(title.capitalize()))
            else:
                passed = True
                for validation in validations:
                    if validation == "phone":
                        if not self.is_phone_valid(user_input):
                            self.printer.print_warning("{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_phone_valid(user_input)
                    if validation == "ssn":
                        if not self.is_ssn_valid(user_input):
                            self.printer.print_warning("{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_ssn_valid(user_input)
                    if validation == "email":
                        if not self.is_email_valid(user_input):
                            self.printer.print_warning("{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_email_valid(user_input)
                    if validation == "year":
                        if not self.is_year_valid(user_input):
                            self.printer.print_warning("{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_year_valid(user_input)
                    if validation == "date":
                        if not self.is_date_valid(user_input):
                            self.printer.print_warning("{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_date_valid(user_input)
                    if validation == "hours":
                        if not self.is_hours_valid(user_input):
                            self.printer.print_warning("{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_hours_valid(user_input)
                if passed:
                    break
        return user_input

    def get_option(self, title, options, current_page = 1, warning_msg = ""):
        options_count = len(options)
        last_page = int(options_count / self.items_per_page) + (options_count % self.items_per_page > 0)
        if current_page > last_page:
            current_page = last_page
        start = (current_page - 1) * self.items_per_page
        end = start + self.items_per_page if not current_page == last_page else options_count

        page = False
        
        if options_count > 0:
            print("Select {}:".format(title))
            for i in range(start, end):
                if isinstance(options[i], list):
                    print("\t{}. {}".format(i+1, options[i][1]))
                else:
                    print("\t{}. {}".format(i+1, options[i].capitalize()))
            if last_page > 1:
                self.printer.new_line()
                print("{}".format("\tPage {} of {}".format(current_page, last_page)))
                print("\t(N)ext page / (P)revious page")

            if not warning_msg == "":
                self.printer.print_warning(warning_msg)
            else:
                self.printer.new_line()

            user_input = input("Choose an option: ")
            if user_input == 'q':
                raise ValueError
            elif user_input == 'n' or user_input == "next":
                page = True
                if current_page >= last_page:
                    current_page = last_page
                    warning_msg = "You are currenly on the last page"
                else:
                    current_page += 1
            elif user_input == 'p' or user_input == "previous":
                page = True
                if current_page > 1:
                    current_page -= 1
                else:
                    current_page = 1
                    warning_msg = "You are currenly on the first page"
            elif not user_input.isnumeric():
                warning_msg = "Please select available option"
            else:
                if len(options) >= int(user_input) and int(user_input) > 0:
                    user_input = options[int(user_input)-1]
                    warning_msg = ""
                else:
                    warning_msg = "Please select available option"
        if not warning_msg == "" or page:
            return (False, warning_msg, current_page)
        if isinstance(user_input, list):
            return (True, user_input[0])
        else:
            return (True, user_input)

    def is_email_valid(self, email):
        email_list = email.split("@")
        try:
            if len(email_list) == 2:
                new_list = email_list[1].split(".")
                final_list = []
                final_list.append(email_list[0])
                final_list.append(new_list[0])
                final_list.append(new_list[1])
                if len(final_list[0]) >= 1 and len(final_list[1]) >= 1 and len(final_list[2]) >= 2:
                    return email
                else:
                    return False 
        except IndexError:
            return False
        else:
            return False
    
    def is_phone_valid(self, phone):
        str_list = []
        for letter in phone:
            try:
                if letter.isdigit() == True:
                    str_list.append(letter)
            except ValueError:
                return False
        if len(str_list) == 10:
            extra = '+'
            list_to_str = ''.join(str(e) for e in str_list)
            new_phone = extra + list_to_str
            return new_phone
        elif len(str_list) == 7:
            areacode = '+354'
            list_to_str = ''.join(str(e) for e in str_list)
            new_phone = areacode + list_to_str
            return new_phone
        elif len(str_list) == 9:
            extra = '+'
            list_to_str = ''.join(str(e) for e in str_list)
            new_phone = extra + list_to_str
            return new_phone
        elif len(str_list) == 12:
            extra = '+'
            list_to_str = ''.join(str(e) for e in str_list)
            new_phone = extra + list_to_str
            return new_phone
        else:
            return False
    
    def is_year_valid(self, year):
        int_list = []
        for number in year:
            try:
                int_year = int(number)
                int_list.append(int_year)
            except ValueError:
                return False
        if len(year) == 4:
            list_to_str = ''.join(str(e) for e in int_list)
            return list_to_str
        else:
            return False  
    
    def is_ssn_valid(self, ssn):
        int_list = []
        for number in ssn:
            try:
                if number != "-":
                    int_ssn = int(number)
                    int_list.append(int_ssn) 
            except ValueError:
                return False
        if len(int_list) == 10:
            list_to_str = ''.join(str(e) for e in int_list)
            return list_to_str
        else: 
            return False

    def is_date_valid(self, date):
            return True

    def is_hours_valid(self, hours):
        #09:00 - 17:00
        return hours