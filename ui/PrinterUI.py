class PrinterUI:
    def __init__(self):
        self.GREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\33[;31m'

        self.END = '\33[;0m'

    def print_success(self, msg):
        print(self.GREEN + msg + self.END)

    def print_warning(self, msg):
        print(self.WARNING + msg + self.END)

    def print_fail(self, msg):
        print(self.FAIL + msg + self.END)

    def print_options(self, msgs):
        for i in range(len(msgs)):
            print("{}. {}".format(i+1, msgs[i]))

    def new_line(self, count = 1):
        print('\n' * (count - 1))

    def header(self, title):
        self.clear()
        print("-" * 50)
        print("|{:^48}|".format(title))
        print("-" * 50)
        print()

    def clear(self):
        print("\033[2J\033[0;0H")