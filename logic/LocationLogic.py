from repositories.MainRepository import MainRepository


class LocationLogic:

    def __init__(self):
        self.rep = MainRepository()

    
    def create(self, location):
        self.rep.create_location(location)

    
    def get_all_locations(self):
        return self.rep.get_all_locations()


    def update(self, id, updates):
        return self.rep.update_location(id, updates)


    def delete(self, id):
        return self.rep.delete_location(id)

    def get_location_by_id(self, id):
        locations = self.get_all_locations()

        for location in locations:
            if location.id == id:
                return location
        return None





