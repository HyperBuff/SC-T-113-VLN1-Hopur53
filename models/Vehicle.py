
class Vehicle:
    def __init__(self, manufacturer: str, model: str, vehicle_type: str, status: str, man_year: str, color: str, licence_type: str, location: str, id = None) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.vehicle_type = vehicle_type
        self.status = status
        self.man_year = man_year
        self.color = color
        self.licence_type = licence_type
        self.location = location

    def set_id(self, id):
        self.id = id