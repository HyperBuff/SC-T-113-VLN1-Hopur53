from ui.PrinterUI import PrinterUI

class InputUI:

    def __init__(self):
        self.printer = PrinterUI()

    def get_input(self, title, validations = []):
        while True:
            user_input = input("\tEnter {}: ".format(title.lower()))
            if user_input == 'q':
                raise ValueError
            elif len(user_input.replace(" ", "")) < 1:
                self.printer.print_warning("\t{} must been at least 1 character".format(title.capitalize()))
            else:
                passed = True
                for validation in validations:
                    if validation == "phone":
                        if not self.is_phone_valid(user_input):
                            self.printer.print_warning("\t{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_phone_valid(user_input)
                    if validation == "ssn":
                        if not self.is_ssn_valid(user_input):
                            self.printer.print_warning("\t{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_ssn_valid(user_input)
                    if validation == "email":
                        if not self.is_email_valid(user_input):
                            self.printer.print_warning("\t{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_email_valid(user_input)
                    if validation == "year":
                        if not self.is_year_valid(user_input):
                            self.printer.print_warning("\t{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_year_valid(user_input)
                    if validation == "date":
                        if not self.is_date_valid(user_input):
                            self.printer.print_warning("\t{} is not valid".format(title.capitalize()))
                            passed = False
                        else:
                            user_input = self.is_date_valid(user_input)
                if passed:
                    break
        return user_input

    def get_option(self, title, options):
        while True:
            print("Select {}:".format(title))
            for i in range(len(options)):
                print("\t{}. {}".format(i+1, options[i].capitalize()))
            user_input = input("\nChoose an option: ")
            if user_input == 'q':
                raise ValueError
            else:
                try:
                    user_input = options[int(user_input)-1]
                    break
                except:
                    pass
        return user_input

    def is_email_valid(self, email):
        email_list = email.split("@")
        if len(email_list) == 2:
            new_list = email_list[1].split(".")
            final_list = []
            final_list.append(email_list[0])
            final_list.append(new_list[0])
            final_list.append(new_list[1])
            if len(final_list[0]) >= 1 and len(final_list[1]) >= 1 and len(final_list[2]) >= 2:
                return True
            else:
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