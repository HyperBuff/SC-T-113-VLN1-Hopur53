from repositories.MainRepository import MainRepository

class EmployeeLogic:

    def __init__(self):
        pass
    
    def get_all_employees(self):
        return MainRepository().get_all_employees()

    def get_user_id_from_email(self, email):
        employees = self.get_all_employees()

        for employee in employees:
            if employee.email == email:
                return employee.id
        return None