<<<<<<< HEAD
from ui.MainUI import MainUI

if __name__ == "__main__":
    ui = MainUI()
=======
from models.Vehicle import Vehicle
from repositories.VehicleRepository import VehicleRepository
from models.Contract import Contract
from repositories.ContractRepository import ContractRepository
from models.Destination import Destination
from repositories.DestinationRepository import DestinationRepository
from models.VehicleType import VehicleType
from repositories.VehicleTypeRepository import VehicleTypeRepository
#ui = MainUI()

if __name__ == "__main__":
    v = VehicleRepository()
    vechicle1 = Vehicle("Doc", "Delorian", "Time Machine", "Good", "1987", "gray", "Highschool Diploma", "Keflavík")
    v.create(vechicle1)
    c = ContractRepository()
    contract1 = Contract("Marty", "8182809", "MartyMcfly@gmail.com", "Time Street 123", "12453", "good", "123241", "Keflavík", "01/12/20", "07/12/20", "01/12/20", "Confirmed", "07/12/20", "1250.50")
    c.create(contract1)
    contract1 = Contract("Marty", "8182809", "MartyMcfly@gmail.com", "Time Street 123", "12453", "good", "123241", "Keflavík", "01/12/20", "07/12/20", "01/12/20", "Confirmed", "07/12/20", "1250.50")
    c.create(contract1)
    d = DestinationRepository()
    destination1 = Destination("Iceland", "Keflavíkurflugvöllur", "4214412", "6:00-23:00")
    d.create(destination1)
    vt = VehicleTypeRepository()
    vechicletype1 = VehicleType("timemachine", "keflavík", "500")
    vt.create(vechicletype1
    )
>>>>>>> 39847254e779679043dd08ff15d5b385de78507c
