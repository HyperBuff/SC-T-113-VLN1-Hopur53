from repositories.MainRepository import MainRepository

class VehicleLogic:

    def __init__(self):
        self.rep = MainRepository()
    
    def create(self, vehicle):
        self.rep.create_vehicle(vehicle)

    def get_all_vehicles(self):
        return self.rep.get_all_vehicles()

    def update(self, id, updates):
        return self.rep.update_vehicle(id, updates)

    def delete(self, id):
        return self.rep.delete_vehicle(id)

    def get_vehicle_by_id(self, id):
        vehicles = self.get_all_vehicles()

        for vehicle in vehicles:
            if vehicle.id == id:
                return vehicle
        return None