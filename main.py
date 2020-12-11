import os
from ui.MainUI import MainUI

# ASNI support for Windows
os.system("color")

# Run software only from main.py
if __name__ == "__main__":
    ui = MainUI()