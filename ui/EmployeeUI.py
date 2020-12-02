from logic.MainLogic import MainLogic

class EmployeeUI:

    def __init__(self):
        self.user_id = None

        self.logic = MainLogic()


    def loop(self):
        pass

    def login(self):

        print("Type in email to login to your account, or q to close the program.")

        action = input("")

        if action == "q":
            return None
        else:
            return self.logic.login(action)
        
