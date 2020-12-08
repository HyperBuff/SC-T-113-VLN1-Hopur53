from repositories.MainRepository import MainRepository

class EmployeeLogic:

    def __init__(self):
        self.rep = MainRepository()
    
    def create(self, employee):
        self.rep.create_employee(employee)

    def get_all_employees(self):
        return self.rep.get_all_employees()

    def update(self, id, updates):
        return self.rep.update_employee(id, updates)

    def delete(self, id):
        return self.rep.delete_employee(id)
 
    def get_user_id_from_email(self, email):
        employees = self.get_all_employees()

        for employee in employees:
            if employee.email == email:
                return employee.id
        return None

    def get_employee_by_id(self, id):
        employees = self.get_all_employees()

        for employee in employees:
            if employee.id == id:
                return employee
        return None

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
                return None 
        else:
            return None


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


    def is_phone_number_valid(self, phone):
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
