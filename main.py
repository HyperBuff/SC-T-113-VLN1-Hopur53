from ui.MainUI import MainUI
from models.Employee import Employee
from repositories.EmployeeRepository import EmployeeRepository
from models.Vehicle import Vehicle
from repositories.VehicleRepository import VehicleRepository
from models.Contract import Contract
from repositories.ContractRepository import ContractRepository


#ui = MainUI()

if __name__ == "__main__":
    e = EmployeeRepository()
    em = Employee("aðalsteinn", "D", "500", "444", "96", "333", "add@f.d")
    e.create(em)
    v = VehicleRepository()
    vechicle1 = Vehicle("Doc", "Delorian", "Time Machine", "Good", "1987", "gray", "Highschool Diploma", "Keflavík")
    v.create(vechicle1)
    c = ContractRepository()
    contract1 = Contract("Marty", "8182809", "MartyMcfly@gmail.com", "Time Street 123", "12453", "good", "123241", "Keflavík", "01/12/20", "07/12/20", "01/12/20", "Confirmed", "07/12/20", "1250.50"
    )
    c.create(contract1)