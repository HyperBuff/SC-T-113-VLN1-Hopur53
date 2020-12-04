from repositories.MainRepository import MainRepository


class DestinationLogic:

    def __init__(self):
        self.rep = MainRepository()

    
    def create(self, destination):
        self.rep.create_destination(destination)

    
    def get_all_destinations(self):
        return self.rep.get_all_destinations()


    def update(self, id, updates):
        return self.rep.update_destination(id, updates)


    def delete(self, id):
        return self.rep.delete_destination(id)




