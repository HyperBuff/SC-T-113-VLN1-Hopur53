from repositories.MainRepository import MainRepository

class VehicleLogic:

    def __init__(self):
        self.rep = MainRepository()
    
    def create(self, vehicle):
        self.rep.create_vehicle(vehicle)

    def get_all_vehicles(self):
        return self.rep.get_all_vehicles()

    def get_all_available_vehicles(self):
        results = []
        for vehicle in self.get_all_vehicles():
            if vehicle.status == "Available":
                results.append(vehicle)
        return results

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

    def filter_vehicles(self, filters):
        results = []
        vehicles = self.get_all_vehicles()
        for vehicle in vehicles:
            valid_vehicle = True
            for key in filters.keys():
                if key == "status": # {"vehicle": vehicle_id}
                    if vehicle.status != filters[key]:
                        valid_vehicle = False
                if key == "location": # {"location": location_id}
                    if vehicle.location_id != filters[key]:
                        valid_vehicle = False
            if valid_vehicle:
                results.append(vehicle)
        return results