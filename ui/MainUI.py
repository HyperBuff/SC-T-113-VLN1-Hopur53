from logic.MainLogic import MainLogic

class MainUI:
    def __init__(self):
        self.user_id = None

        if self.user_id == None:
            self.select_user()
        else:
            print(self.user_id)
            

    def select_user(self):

        users = MainLogic().get_em()
        users_output = ""

        for i in range(len(users)):
            users_output += f"{i+1}. {users[i]}\n"

        print(f"------------ Main Menu ------------\n\n\t\tSelect User\n\n-----------------------------------\n\n" + users_output + "\n\n-----------------------------------")
        input("User to select: ")