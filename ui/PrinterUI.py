class PrinterUI:
    def __init__(self):
        self.GREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'

        self.END = '\033[0m'

    # Prints success messages (GREEN)
    def print_success(self, msg):
        print(self.GREEN + msg + self.END)

    # Print warning messages (YELLOW)
    def print_warning(self, msg):
        print(self.WARNING + msg + self.END)
    
    # Print static messages (RED)
    def print_fail(self, msg):
        print(self.FAIL + msg + self.END)

    # Prints optons from list
    def print_options(self, msgs):
        for i in range(len(msgs)):
            print("{}. {}".format(i+1, msgs[i]))

    # Print menu options
    def print_menu_options(self, menu):
        for i in range(len(menu.keys())):
            print("{}. {}".format(i+1, list(menu.keys())[i]))

    # Prints new lines
    def new_line(self, count = 1):
        print('\n' * (count - 1))

    # Prints header for every screen
    def header(self, title):
        self.clear()
        print("-" * 50)
        print("|{:^48}|".format(title))
        print("-" * 50)
        print()

    # Clear screen
    def clear(self):
        print("\033[2J\033[0;0H")