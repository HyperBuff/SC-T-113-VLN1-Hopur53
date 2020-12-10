from repositories.Repository import Repository
from models.Vehicle import Vehicle


class VehicleRepository:

    def __init__(self):
        self.filename = 'data/vehicle.csv'
        self.fieldnames = ['manufacturer', 'model', 'vehicle_type_id', 'status', 'man_year', 'color', 'licence_type', 'location_id', 'id']

    def create(self, vehicle: Vehicle):
        row = dict((key, getattr(vehicle, key)) for key in self.fieldnames)
        Repository().create(self.filename, self.fieldnames, row)
        return vehicle

    def read(self):
        rows = Repository().read(self.filename)
        vehicles = [Vehicle(row['manufacturer'], row['model'], row['vehicle_type_id'], row['status'], row['man_year'], row['color'], row['licence_type'], row['location_id'], row['id']) for row in rows]
        return vehicles
    
    def update(self, id, updates: dict):
        return Repository().update(self.filename, self.fieldnames, id, updates)

    def delete(self, id) -> None:
        return Repository().delete(self.filename, self.fieldnames, id)