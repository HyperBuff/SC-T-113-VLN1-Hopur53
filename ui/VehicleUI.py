#from logic.MainLogic import MainLogic
#from models.Vehicle import Vehicle

class VehicleUI:

    #def __init__(self):
        #self.logic = MainLogic()

    def menu(self):
        action = ''
        while not action == 'q':
            print("\n\n1. Register New Vehicle\n2. View Vehicle Information\n3. Modify Vehicle Information\n4. View Vehicle Status\n\n\33[;31mPress q to go back\33[;0m\n")
            action = input("\nChoose an option: ").lower()

            if action == str(1):
                self.create()
            elif action == str(2):
                self.read()
            elif action == str(3):
                self.update()
            elif action == str(4):
                self.delete()
            elif action == str(5):
                pass

    def create(self):
        #self.header("Add vehicle")
        print("Enter vehicle details:")
        
        manufacturer = input("\tEnter manufacturer: ")
        model = input("\tEnter model: ")
        vehicle_type = input("\tEnter vehicle type: ")
        man_year = input("\tEnter manufacture year: ")
        color = input("\tEnter color: ")
        license_type = input("\tEnter license required: ")
        location = input("\tEnter location: ")
        renting_rate = input("\Enter renting rate: ")
   

        #new_vehicle = (manufacturer: str, model: str, vehicle_type: str, status: str, man_year: str, color: str, licence_type: str, location: str)
        #return self.logic.create_employee(new_vehicle)          

    
    def read(self):
        pass


    def update(self):
        pass

    def delete(self):
        pass
    


