from repositories.MainRepository import MainRepository

class EmployeeLogic:

    def __init__(self):
        pass
    
    def get_list_of_employee(self):
        return MainRepository().get_all_employee()