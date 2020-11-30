from ui.MainUI import MainUI

from models.Employee import Employee
from repositories.EmployeeRepository import EmployeeRepository



if __name__ == "__main__":
    e = EmployeeRepository()


    employee1 = Employee("Aðalsteinn", "Duggufjara", "600", "0907982949", "6494444", "4611561", "aleifsm@gmail.com")

    e.create(employee1)