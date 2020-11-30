import uuid

from repositories.Repository import Repository
from models.Vehicle import Vehicle


class VehicleRepository:

    def __init__(self):
        self.filename = 'data/vehicle.csv'
        self.fieldnames = ['manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'licence_type', 'location', 'id']

    def create(self, vehicle: Vehicle):
        vehicle.set_id(self.generate_id())
        row = dict((key, getattr(vehicle, key)) for key in self.fieldnames)
        print(row)
        Repository()._create(self.filename, self.fieldnames, row)
        return vehicle

    def read(self):
        rows = Repository()._read(self.filename)
        vehicles = [Vehicle(row['manufacturer'], row['model'], row['vehicle_type'], row['status'], row['man_year'], row['color'], row['licence_type'], row['location'], row['id']) for row in rows]
        return vehicles
    
    def update(self, id, updates: dict):
        return Repository()._update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository()._delete(self.filename, self.fieldnames, id)

    def generate_id(self):
        return str(uuid.uuid4())