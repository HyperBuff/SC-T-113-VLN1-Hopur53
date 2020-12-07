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
            return True
        else: 
            return False

    def is_phone_valid(self, phone):
        """Checks if phone number input is valid."""
        whole_list = []
        digit_list = []
        for every in phone:
            whole_list.append(every)
        if whole_list[3] == "-" and whole_list[7] == "-":
            for number in whole_list:
                try:
                    if number != "-":
                        int_number = int(number)
                        digit_list.append(int_number)
                except ValueError:
                    return False
            if len(digit_list) == 10:
                return True
            else:
                return False
        else:
            for number in phone:
                try:
                    int_number = int(number)
                    digit_list.append(int_number)
                except ValueError:
                    return False
            if len(digit_list) == 7:
                return True
            else:
                return False

    def is_year_valid(self, year):
        return True

    def is_date_valid(self, date):
        return True