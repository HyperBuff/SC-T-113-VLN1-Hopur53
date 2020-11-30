from ui.MainUI import MainUI

from models.Employee import Employee
from repositories.EmployeeRepository import EmployeeRepository
from models.Vehicle import Vehicle
from repositories.VehicleRepository import VehicleRepository


ui = MainUI()


"""
if __name__ == "__main__":
    e = EmployeeRepository()
<<<<<<< HEAD

    em = Employee("aðalsteinn", "D", "500", "444", "96", "333", "add@f.d")

    e.create(em)
"""
=======
    v = VehicleRepository()

    employee1 = Employee("Aðalsteinn", "Duggufjara", "600", "0907982949", "6494444", "4611561", "aleifsm@gmail.com")
    vechicle1 = Vehicle("Doc", "Delorian", "Time Machine", "Good", "1987", "gray", "Highschool Diploma", "Keflavík")
    e.create(employee1)
    v.create(vechicle1)
    
>>>>>>> e79e9dfef13e8030015b703c2c1884fba78eadbf
