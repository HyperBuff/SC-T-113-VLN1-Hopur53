from repositories.Repository import Repository
from models.Location import Location


class LocationRepository:

    def __init__(self):
        self.filename = 'data/location.csv'
        self.fieldnames = ['country', 'airport', 'phone', 'hours', 'id']

    def create(self, location: Location):
        row = dict((key, getattr(location, key)) for key in self.fieldnames)
        Repository().create(self.filename, self.fieldnames, row)
        return location

    def read(self):
        rows = Repository().read(self.filename)
        locations = [Location(row['country'], row['airport'], row['phone'], row['hours'], row['id']) for row in rows]
        return locations
    
    def update(self, id, updates: dict):
        return Repository().update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository().delete(self.filename, self.fieldnames, id)