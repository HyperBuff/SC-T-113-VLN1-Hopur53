import uuid

from repositories.Repository import Repository
from models.VehicleType import VehicleType


class VehicleTypeRepository:

    def __init__(self):
        self.filename = 'data/vehicletype.csv'
        self.fieldnames = ['name', 'regions', 'rate', 'id']

    def create(self, vehicletype: VehicleType):
        row = dict((key, getattr(vehicletype, key)) for key in self.fieldnames)
        Repository()._create(self.filename, self.fieldnames, row)
        return vehicletype

    def read(self):
        rows = Repository()._read(self.filename)
        vehicletypes = [VehicleType(row['name'], row['regions'], row['rate'], row['id']) for row in rows]
        return vehicletypes
    
    def update(self, id, updates: dict):
        return Repository()._update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository()._delete(self.filename, self.fieldnames, id)

    def generate_id(self):
        return str(uuid.uuid4())