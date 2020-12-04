from repositories.MainRepository import MainRepository

class EmployeeLogic:

    def __init__(self):
        self.rep = MainRepository()
    
    def create(self, employee):
        self.rep.create_employee()

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
    


    