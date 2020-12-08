from repositories.MainRepository import MainRepository

class VehicleTypeLogic:

    def __init__(self):
        self.rep = MainRepository()
    
    def create(self, vehicle):
        self.rep.create_vehicletype(vehicle)

    def get_all_vehicletypes(self):
        return self.rep.get_all_vehicletypes()

    def update(self, id, updates):
        return self.rep.update_vehicletype(id, updates)

    def delete(self, id):
        return self.rep.delete_vehicletype(id)

    def get_vehicletype_by_id(self,id):
        vehicletypes = self.get_all_vehicletypes()

        for vehicletype in vehicletypes:
            if vehicletype.id == id:
                return vehicletype
        return None