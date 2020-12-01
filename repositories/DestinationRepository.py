from repositories.Repository import Repository
from models.Destination import Destination


class DestinationRepository:

    def __init__(self):
        self.filename = 'data/destination.csv'
        self.fieldnames = ['country', 'airport', 'phone', 'hours', 'id']

    def create(self, destination: Destination):
        row = dict((key, getattr(destination, key)) for key in self.fieldnames)
        Repository()._create(self.filename, self.fieldnames, row)
        return destination

    def read(self):
        rows = Repository()._read(self.filename)
        destinations = [Destination(row['country'], row['airport'], row['phone'], row['hours'], row['id']) for row in rows]
        return destinations
    
    def update(self, id, updates: dict):
        return Repository()._update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository()._delete(self.filename, self.fieldnames, id)