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

    def get_employee_by_id(self, user_id):
        employees = self.get_all_employees()

        for employee in employees:
            if employee.id == user_id:
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
                return None
        if len(int_list) == 10:
            return True
        else: 
            return None

    def is_phone_number_valid(self, phone):
        if phone == "test":
            return False
        return True
